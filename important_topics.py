################################################# *IMPORTANT TOPICS* ##############################
### Raft Ordering Service ###
	* Raft is a crash fault tolerant (CFT) ordering service based on an implementation of Raft protocol in *etcd*.
	* It uses a “leader and follower” model, in which a leader is dynamically elected among the ordering nodes in a channel (this collection of nodes is known as the “consenter set”), and that leader replicates messages to the follower nodes.
	* Because the system can sustain the loss of nodes, including leader nodes, as long as there is a majority of ordering nodes (what’s known as a “quorum”) remaining, Raft is said to be “crash fault tolerant” (CFT).
	* Advantages of Raft Over Kafka:
		* There is no functional difference between an ordering service based on Raft versus Kafka.
		* Raft is easier to set up. (Because With Raft, everything is embedded into your ordering node.)
		* With Raft, each organization can have its own ordering nodes, participating in the ordering service, which leads to a more decentralized system. Given that, having ordering nodes run by different organizations when using Kafka (which Fabric supports) doesn’t give you much in terms of decentralization because the nodes will all go to the *same Kafka cluster* which is under the *control of a single organization*.
		* Raft is supported natively, but with kafka & zookeeper, users are required to get the requisite images and learn how to use it of their own.
		* Fabric Raft Implementation has been developed and will be supported within the Fabric developer community.
		* Raft allows the users to specify which ordering nodes will be deployed to which channel.In this way, peer organizations can make sure that, if they also own an orderer, this node will be made a part of a ordering service of that channel,
	* Note: 
		* Similar to Solo and Kafka, a Raft ordering service can lose transactions after acknowledgement of receipt has been sent to a client. For example, if the leader crashes at approximately the same time as a follower provides acknowledgement of receipt. Therefore, application clients should listen on peers for transaction commit events regardless (to check for transaction validity), but extra care should be taken to ensure that the client also gracefully tolerates a timeout in which the transaction does not get committed in a configured timeframe. Depending on the application, it may be desirable to resubmit the transaction or collect a new set of endorsements upon such a timeout.
		
		
### Raft Concepts ###
	1) Log:
		* Full sequence of *Log Entry* which is a primary unit of work for Raft ordering service.
		* We consider the log consistent if a majority (a quorum, in other words) of members agree on the entries and their order, making the logs on the various orderers replicated.
	2) Consenter Set:
		* The ordering nodes actively participating in the consensus mechanism for a given channel and receiving replicated logs for the channel.
		* This can be all of the nodes available (either in a single cluster or in multiple clusters contributing to the system channel), or a subset of those nodes.
	3) Finite-State Machine (FSM):
		* Every ordering node in Raft has an FSM and collectively they’re used to ensure that the sequence of logs in the various ordering nodes is deterministic (written in the same sequence).
	4) Quorum:
		* Quorum is a majority of nodes for every consenter set.
		* If a quorum of nodes is unavailable for any reason, the ordering service cluster becomes unavailable for both read and write operations on the channel, and no new logs can be committed.
	5) Leader:
		* Leader is responsible for ingesting new log entries, replicating them to follower ordering nodes, and managing when an entry is considered committed. 
		* Channel’s consenter set(All Ordering Nodes) elects a single node to be the leader.
		* This is not a special type of orderer.
		* It is only a role that an orderer may have at certain times, and then not others, as circumstances determine.
	6) Follower:
		* Followers receive the logs from the leader.
		* Followers also receive “heartbeat” messages from the leader.
		* In the event that the leader stops sending those message for a configurable amount of time, the followers will initiate a leader election and one of them will be elected the new leader.




### How leader election works in Raft ###
	* The process of electing a leader happens within the orderer’s internal processes.
	* Raft nodes are always in one of three states: follower, candidate, or leader. 
	* All nodes initially start out as a follower. In this state, they can accept log entries from a leader (if one has been elected), or cast votes for leader. If no log entries or heartbeats are received for a set amount of time (for example, five seconds), nodes self-promote to the candidate state. In the candidate state, nodes request votes from other nodes. If a candidate receives a quorum of votes, then it is promoted to a leader. The leader must accept new log entries and replicate them to the followers.



### Snapshotting ###
	* If an ordering node goes down, Raft uses a process called “snapshotting” is used, in which users can define how many bytes of data will be kept in the log to keep all logs indefinitely, in order to save disk space.
	* This amount of data will conform to a certain number of blocks (which depends on the amount of data in the blocks. Note that only full blocks are stored in a snapshot).
	* For example, let’s say lagging replica R1 was just reconnected to the network. Its latest block is 100. Leader L is at block 196, and is configured to snapshot at amount of data that in this case represents 20 blocks. R1 would therefore receive block 180 from L and then make a Deliver request for blocks 101 to 180. Blocks 180 to 196 would then be replicated to R1 through the normal Raft protocol.


###################################################################################################




