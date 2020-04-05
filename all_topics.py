#################################################     *ALL TOPICS*     ##################################################
### Blockchain and its Features ###
	* Decentralized --- Replication of ledger across the n/w participants in a blockchain network.
	* Collaboration --- Replication of ledger with, each of whom collaborate in its maintenance.
	* Systems of Proof --- "Immutability" of transactions in ledger makes it simple to determine the provenance of information
	* Applications --- By means of "Smart Contracts" which has a business logic. 
	* Consensus --- Process of keeping the ledger transactions synchronized across the network (Achieved by - updating same transaction in same order.)
	* Shared --- A blockchain system has shared programs (smart contracts) to update shared ledgers but in today’s systems, where a participant’s private programs are used to update their private ledgers



### Hyperledger Fabric ###
	* Open source enterprise-grade permissioned distributed ledger technology (DLT) platform.
	* Established under the Linux Foundation (Open Governance).
	* Has a highly modular and configurable architecture.
	* First DLT to support smart contracts authored in general-purpose programming languages such as Java, Go and Node.js.
	* Support for pluggable consensus protocols that enable the platform to be more effectively customized to fit particular use cases and trust models.
	* Can leverage consensus protocols that do not require a native cryptocurrency to incent costly mining or to fuel smart contract execution.
	* Enables confidentiality through its channel architecture and private data feature.
	
	
	
	
### Modular Components in Fabric ###
	* Pluggable Ordering Service
		--- Establishes consensus on the order of transactions and then broadcasts blocks to peers.
	* Pluggable Membership Service Provider
		--- Is responsible for associating entities in the network with cryptographic identities.
	* Optional Peer-To-Peer Gossip Service
		--- Disseminates the blocks output by ordering service to other peers.
	* Smart Contracts
		--- Run within a container environment (e.g. Docker) for isolation and can be written in standard programming langs
	* Ledger
		--- Can be configured to support a variety of DBMSs.
	* Pluggable Endorsement and Validation Policy Enforcement
		--- Can be independently configured per application. 
	
	
		
### New Approach in Fabric ###
	* Replacing order-execute fashion with *Execute-Order-Validate* model.
	* Execute a transaction and check its correctness, thereby endorsing it,
	* Order transactions via a (pluggable) consensus protocol, and
	* Validate transactions against an application-specific endorsement policy before committing them to the ledger.
	* First phase (1st point) also eliminates any non-determinism, as inconsistent results can be filtered out before ordering
	
	
	
	
### Performance of Fabric ###
	* Performance of a blockchain platform can be affected by many variables such as transaction size, block size, network size, as well as limits of the hardware, etc.
	* The latest scaled Fabric to 20,000 transactions per second.
	
	
	
### Choosing Pluggable Consensus Protocol ###
	* When deployed within a single enterprise, or operated by a trusted authority,
		--- crash fault-tolerant (CFT) consensus protocol might be more than adequate
	* In a multi-party, decentralized use case,
		--- a more traditional byzantine fault tolerant (BFT) consensus protocol might be required.
		
		
		
		
### Application-Specific Endorsement Policy ###
### For Transaction Endorsement ###
	* Every Smart Contract inside a chaincode package has an Endorsement Policy.(not to be confused with chaincode endorsement)
	* Specifies which peer nodes, or how many of them, belonging to different channel members need to execute and validate a transaction against a given smart contract in order for the transaction to be considered valid.
	* Hence, the endorsement policies define the organizations (through their peers) who must “endorse” (i.e., approve of) the execution of a proposal.
	* Each transaction need only be executed (endorsed) by the subset of the peer nodes necessary to satisfy the transaction’s endorsement policy.
	* Fabric lifecycle allows you to change an endorsement policy or private data collection configuration without having to repackage or reinstall the chaincode. 
	
	
	* The *Endorsement Policy* is the *default endorsement policy*.	
	* Endorsement policy is specified for a *chaincode (smart contracts - imp.)* when it is approved and committed to the channel using the Fabric chaincode lifecycle.
	* *One Endorsement Policy* covers all of the *state* associated with a chaincode.
	* Endorsement policy can be specified either by reference to an endorsement policy defined in the channel configuration or by explicitly specifying a Signature policy.
	* If an endorsement policy is not explicitly specified during the approval step, the default Endorsement policy "MAJORITY Endorsement" is used which means that a majority of the peers belonging to the different channel members (organizations) need to execute and validate a transaction against the chaincode in order for the transaction to be considered valid. 
	* This default policy allows organizations that join the channel to become automatically added to the chaincode policy.
	* If you don’t want to use the default endorsement policy, use the Signature policy format to specify a more complex endorsement policy. (It also allow you to include *principals*)
	* Principals are described as ‘MSP.ROLE’, where MSP represents the required MSP ID (the organization), and ROLE represents one of the four accepted roles: Member, Admin, Client, and Peer.
	* Some examples of valid principals are:
		* ‘Org0.Admin’: an administrator of the Org0 MSP
		
		
	# State-Based Endorsement Policy #
	* There are cases where it may be necessary for a Particular State (a particular key-value pair, in other words) to have a different endorsement policy. 
	* For this, state-based endorsement allows the default chaincode-level endorsement policies to be overridden by a different policy for the specified keys.
	
	
	
	
	
### Chaincode Endorsement Policies ###
### For Chaincode Package Endorsement ###
	* The *LifecycleEndorsement Policy* governs who needs to approve a *chaincode definition*. (for chaincodes package)
	
		
	
	
### Distributed Ledger ###
	* Distributed Ledger is used to encapsulate the **Shared Information** in a network.
	* Is a combination of the two components, world state *Database* and the transaction log *History*.
	* Single ledger can have one or more smart contracts.
	* Legder physically hosted on Peer, but logically hosted on the channel.
	* 1)World State Database
		* Describes the state of the ledger at a given point in time.
		* It’s the database of the ledger.
		* The world state database could be a relational data store, or a graph store, or a temporal database.
		* A database that holds *current values* of a *set of ledger states*.
		* Ledger states are, by default, expressed as key-value pairs with the Version Number.
		* Note that Version Number is for Every State in a ledger.
		* The version number is for internal use by Hyperledger Fabric, and is incremented every time the state changes.
		* The version is checked whenever the state is updated to make sure the current states matches the version at the time of endorsement.
		* This ensures that the world state is changing as expected; that there has not been a concurrent update.
		* World State can be re-generated from the blockchain at any time. 
		* LevelDB is the default and is particularly appropriate when ledger states are simple key-value pairs. 
		* CouchDB is a particularly appropriate choice when ledger states are structured as JSON documents because CouchDB supports the rich queries and update of richer data types often found in business transactions.
		* Implementation-wise, CouchDB runs in a separate operating system process, but there is still a 1:1 relation between a peer node and a CouchDB instance, unlike LevelDB runs in a same operating system process.
		* All of this is invisible to a smart contract.
		* World states are in a *Namespace* so that only smart contracts within the same chaincode can access a given namespace.
	* 2)Transaction Log History
		* Blockchain is always implemented as a File.
		* Immutably records all transactions which have resulted in the current value of the world state.
		* Sequenced, tamper-resistant record of all state transitions in the fabric.
		* It’s the update history for the world state.
		* Transaction Log History (Blockchain) determines the *World State* of the Ledger.
		* Blockchain has recorded *every previous version of each ledger state* and how it has been changed.
		* Blockchain is structured as sequential log of interlinked blocks, where each block contains a sequence of transactions, each transaction representing a query or update to the world state.
		* Each block’s header includes a hash of the block’s transactions (each hash for every transaction in a current block only), as well a hash of the prior block’s header.
		* Genesis Block is the starting point for the ledger, though it does not contain any User Transactions.
		* Genesis Block contains a Configuration Transaction containing the initial state of the network channel.
		* A blockchain is not namespaced beacause,It contains transactions from many different smart contract namespaces.
	* Each participant has a copy of the ledger to every Hyperledger Fabric network they belong to.
	* Described as decentralized because it is replicated across many network participants, each of whom collaborate in its maintenance.
	* Ledgers *cannot fork* the way they do in many other distributed and permissionless blockchain networks here fabric uses Deterministic Consensus Algorithm in an Ordering Service.
	
	
	
	
	
### Blocks ###
	* Blocks consists of three sections:
		1) Block Header:
			* This section comprises three fields, written when a block is created.	
				1) Block number: An integer starting at 0 (the genesis block), and increased by 1 for very new block appended to the blockchain.
				2) Current Block Hash:         The hash of all the transactions contained in the current block.
				3) Previous Block Header Hash: The hash from the previous block header.
				
		2) Block Data:
			* This section contains a list of transactions arranged in order (sequentially).
			* Every Transaction consists of the following fields:
				1) Header: A metadata about transaction (for eg, name of the relevant chaincode, and its version).
				2) Signature: Contains a cryptographic signature, created by the client application. It requires the application’s private key to generate it. (Tamper-Resistant Check)
				3) Proposal: Encodes the input parameters supplied by an application to the smart contract which creates the proposed ledger update. When the smart contract runs, this proposal provides a set of input parameters,which, in combination with the current world state, determines the new world state.
				4) Response: Captures the before and after values of the world state, as a Read Write set(RW-set). It’s the output of a smart contract, and if the transaction is successfully validated, it will be applied to the ledger to update the world state.
				5) Endorsements: This is a list of signed transaction responses from each required organization sufficient to satisfy the endorsement policy. whereas only one transaction response is included in the transaction, there are multiple endorsements.
		3) Block Metadata:
			* This section contains the certificate and signature of the Block Creator which is used to verify the block by network nodes. 
			* Subsequently, the block committer adds a Valid/Invalid Indicator for every transaction into a bitmap that also resides in the block metadata, as well as a hash of the cumulative state updates up until and including that block, in order to detect a state fork. 
			* Unlike the block data and header fields, this section is not an Input to the *Block Hash Computation*.
	
	
	
	
	
### 3-Phase Process of UPDATE QUERY TRANSACTION WORKFLOW ###
### entire transaction workflow process is called consensus ###
	* Specifically, applications that want to update the ledger are involved in a 3-phase process, which ensures that all the peers in a blockchain network keep their ledgers consistent with each other.
	
	* Phase 1: --- Proposal
		* Applications generates transaction proposal which they send to each of the required set of peers (as per the *Endorsement Policy* defined for a Chaincode) for endorsement.
		* Each of these endorsing peers then independently executes a chaincode using the transaction proposal to generate a transaction proposal response which is endorsed by adding Digital Signature. 
		* It does not apply this update to the ledger, but rather simply signs the entire payload using its private key and returns it to the application.
		* Once the application has received a sufficient number of signed proposal responses, the first phase of the transaction flow is complete. 
		* An application can simply request a more up-to-date proposal response when the peer return inconsistent transaction responses for the same transaction proposal.
		
	* Phase 2: --- Ordering and Packaging transactions into Blocks
		* Orderer receives transactions containing endorsed transaction proposal responses from many applications, and orders (sequencing) the transactions and packaging them into blocks,ready for distribution to the peers.
		
	* Phase 3: --- Validation and Commit
		* It involves the distribution and subsequent validation of blocks from the orderer to the peers, where they can be committed to the ledger.
		* When a new block is generated, all of the peers connected to the orderer will be sent a copy of the new block.
		* Upon receipt of a block, a peer will process each transaction in the sequence in which it appears in the block.
		* For every transaction, each peer will verify that the transaction has been endorsed by the required organizations according to the *Endorsement Policy* of the chaincode which generated the transaction. 
		* This process of validation verifies that all relevant organizations have generated the same outcome or result.
		* If a transaction has been endorsed correctly, the peer will attempt to apply it to the ledger.
		* To do above step, a peer must perform a *Ledger Consistency Check* to verify that the current state of the ledger is compatible with the state of the ledger when the proposed update was generated.
		* This may not always be possible, even when the transaction has been fully endorsed.
		* Failed transactions (in consistency check) after fully endorsed, are not applied to the ledger, but they are retained for audit purposes, as are successful transactions.
		* Invalidated (Failed) transactions are still retained in the immutable block created by the orderer, but they are marked as invalid by the peer and do not update the ledger’s state.
		* Finally, every time a block is committed to a peer’s ledger after consistency check with ledger is successfull, that peer generates an appropriate event.
	* Events
		1) *Block Events* include the full block content.
		2) Block *Transaction Events* include summary information only, such as whether each transaction in the block has been validated or invalidated.
		3) *Chaincode Events* that the chaincode execution has produced can also be published at this time.
		
	
	
### Features of Fabric Ledger ###
	* Query and update ledger using key-based lookups, range queries, and composite key queries.
	* Read-only queries using a rich query language (if using CouchDB as state database).
	* Read-only history queries — Query ledger history for a key, enabling data provenance scenarios.
	
	
	
### Transactions ###
	* Consist of the versions of keys/values that were read in chaincode (read set) and keys/values that were written in chaincode (write set).
	* Contain signatures of every endorsing peer and are submitted to ordering service.
	* Are ordered into blocks and are “delivered” from an ordering service to peers on a channel.
	
	
	
	
	
### Peer ###
	* Peers can be created, started, stopped, reconfigured, and even deleted.
	* Every peer node in a channel is a *Committing Peer*.
	* To actually be an *Endorsing Peer*, the smart contract on the peer must be used by a client application to generate a digitally signed transaction response.
	* When an organization has multiple peers in a channel, a *Leader Peer* is a node which takes responsibility for distributing blocks of transactions from the orderer to the other committing peers in the organization.
	* If a peer in one organization needs to communicate with a peer in another organization, then it can use one of the *Anchor Peers* defined in the channel configuration for that organization.
	* Anchor peer can help with many different cross-organization communication scenarios.
	* A peer can be a committing peer, endorsing peer, leader peer and anchor peer all at the same time!
	* Only the anchor peer is optional.
	* For all practical purposes, there will always be a leader peer and at least one endorsing peer and at least one committing peer.
	* Peers provide the control point for access to, and management of, channels.
	* Each peer node (belongs to one org.)in a channel uses the copy of Channel Configuration to determine the operations that respective organizations` client applications can perform.
	* Each peer maintains a copy of the channel configuration for each channel of which they are a member. 
	* Once Peer is started, it can join channel using the *Orderer* by raising the join request to orderer.
	* Each peer maintains a copy of the ledger for each channel of which they are a member.
	* Single peer actually hosts one or more *Instances* of the Ledger.
	* Peer can install one or more smart contracts (Instances) for a single ledger.
	* Peers also have special *System Chaincodes*.
	* Peers and orderers can communicate with each other using channel.
	* Each and every peer in the network is assigned a digital certificate by an administrator from its owning organization.
	* Peer can only run a smart contract and further can take part in the process of transaction endorsement if it is installed on it, but it can know about the interface of a smart contract by being connected to a channel.
	* Validate transactions by verifying the transaction signatures against endorsement policies and enforce the policies.
	* Prior to appending a block (commit to ledger) after validating the transactions, a versioning check is performed to ensure that states for assets that were read have not changed since chaincode execution time. (protection against the double spend).
	* At each of the committing peers, distributed transactions from orderers are recorded, whether valid or invalid, and their local copy of the ledger updated appropriately.
	* It’s not really important where the peer is physically located — it could reside in the cloud, or in a data centre owned by one of the organizations, or on a local machine — it’s the *digital certificate associated with it* that identifies it as being owned by a particular organization.
	* For Example, P3 could be hosted in Org1’s data center, but as long as the digital certificate associated with it is issued by CA2, then it’s owned by Org2.
	* If a peer happens to be down at the time of block distribution by the orderer, or joins the channel later, it will receive the blocks after reconnecting to an ordering service node, or by gossiping with another peer.
	* Peers and Applications do not need to know who the leader node is at any particular time (only ordering nodes know).
		
		
		
### Smart Contracts ###
	* Business logic of a blockchain application.
	* Functions as a trusted distributed application.
	* Smart Contracts is used to encapsulate the **Shared Processes** in a network.
	* Are used to generate transactions.
	* More no. of smart contracts are packaged into a *Chaincode*.
	* Every smart contract inside a chaincode package has an Endorsement Policy. --- For Transaction Endorsement
	* *Chaincode Package* must have been installed on *Peers* by an administrator of the (respective peer) organization, and then defined on a *Channel*.
	* Installing a smart contract shows how we think of it being *Physically Hosted* on a peer, whereas a smart contract that has been defined on a channel shows how we consider it *Logically Hosted* by the channel.
	* State transitions are a result of chaincode invocations, recorded as transactions.
	* X.509 certificates are used in smart contract (transaction responses) to digitally sign transactions.
	* Invoked by an application external to the blockchain when that application needs to interact with the ledger.
	* Chaincode interacts only with the database component of the ledger, the world state (querying it, for example), and not the transaction log.
	* It is possible for a Single Smart Contract which accesses more ledger instaces in a peer (must be configured in this way)
	* Many smart contracts run concurrently in the network.
	* They may be deployed dynamically (in many cases by anyone)
	* Application code should be treated as untrusted, potentially even malicious.
	* In reality, each chaincode has its *Own World State* (of respective ledger--- check this) that is separate from all other chaincodes. 
	* Traditionally, chaincodes are launched by the peer, and then connect back to the peer.
	* In modern approach, now possible to run *Chaincode As an External Service*, for example in a Kubernetes pod, which a peer can connect to and utilize for chaincode execution.
	
	
	
### Orderers ###
	* Orderers, service as a *Network Administration Point* for the fabric network.
	* When orderers receives join request from peers, it uses the *Policy* in the *Channel Configuration* to determine Peer’s permissions on the requeted channel by using peer`s identity.
	* Orderer is initially configured and started by an administrators (of anyone org.) according to a *Network Configuration*.
	* Ordering service node (for eg,O4) is the actor that creates consortia(for eg,2) and channels.
	* Orderer(s) must be hosted by any one (or more) of the organization in a network as per *Network Configuration*.(2 points)
	* Also supports application channels, for the purposes of transaction ordering into blocks for distribution.
	* It can order transactions for one or more application channels.
	* Ordering service node (for eg,O4) has a copy of the network configuration, but in a *Multi-Node Configuration*, every ordering service node will have its own copy of the network configuration.
	* Ordering service node is the distribution point for transactions.
	* Ordering service node gathers endorsed transactions from applications and orders them into transaction blocks, which are subsequently distributed to every peer node in the channel.
	* Two Roles for Single Orderer:
		* At the channel level, orderer role is to gather transactions and distribute blocks inside channel according to the policies defined in channel configuration.
		* At the network level, orderer role is to provide a management point for network resources according to the policies defined in network configuration.
		* Notice again how these roles are defined by different policies within the channel and network configurations respectively.
	* Whether acting as a network management point, or as a distributor of blocks in a channel, its nodes(orderers) can be distributed as required throughout the multiple organizations in a network.
	* Ordering service nodes (multiple orderers) are connected via the *System Channel* which operates a Mini-Blockchain.
	* Orderers also enforce basic access control for channels, restricting who can read and write data to them, and who can configure them.  
	* Ordering service nodes receive transactions from many different application clients concurrently.
	* Blocks created by the orderer are then saved to the orderer’s ledger & distributed to all peers that have in a channel.
	* Sequencing of transactions in a block is not necessarily the same as the *Order* received by the ordering service.
	* Importantly, ordering service puts the transactions into a *strict order*, and peers will use this order when validating and committing transactions.
	* In Raft, transactions (in the form of proposals or configuration updates) are automatically routed by the ordering node that receives the transaction to the current leader of that channel.
	* Only the Ordering Nodes need to know who the leader node is at any particular time (not by peers & applications).
	* When the orderer validation checks have been completed, the transactions are ordered, packaged into blocks, consented on, and distributed.
	
	
	
### Organization ###
	* Every organizations in a n/w has a preferred Certificate Authority.
	* Administrative rights of organization at a network level is decided by the *Network Configuration*.(creating consortia..)
	* When an organization has multiple peers in a channel, it can choose the peers upon which it installs smart contracts; it does not need to install a smart contract on every peer.
	* Approval of a chaincode definition occurs at the organization level.
	* A sufficient number of organizations (orgs administrator) need to approve a *Chaincode Definition*(not transactions generated by the smart contracts) (A majority, by default) before the chaincode definition can be committed to the channel and used to interact with the channel ledger. ----- *LIFECYCLE ENDORSEMENT POLICY*
	* Organization’s peers can have one or more leaders connected to the ordering service to improve resilience and scalability
	* An organization can have zero or more anchor peers defined for it.
	* Every organization has their own set of peers.
	* Every organization has client applications.
	* A new organization(suppose, if added in a channel) can use the chaincode as soon as they approve the chaincode parameters already agreed to by other members of the channel and then installs the chaincode package. 
	* A newly added organization in a channel can approve the chaincode definition once and join multiple peers to the channel with the chaincode package installed.
	* If a newly added organization in a channel, wanted to change the chaincode definition, all members of a channel would need to approve a new definition for their organization, and then one of the organizations would need to commit the definition to the channel.
	* Different organizations may use different Root CAs, or the same Root CA with different Intermediate CAs. 
	* Every organization participating in a channel must have an *Single MSP*( Both Node & Orderer Local MSP) defined for it.
	* An organization can also be divided into multiple Organizational Units (OU), each of which has a certain set of responsibilities, also referred to as *Affiliations*.
	* Specifying OUs is optional. If OUs are not used, all of the identities that are part of an MSP — as identified by the Root CA and Intermediate CA folders — will be considered members of the organization.
	* Organization Units (OUs) are defined in the Fabric CA client configuration file and can be associated with an identity when it is created.
	* In Fabric, NodeOUs provide a way to classify identities in a *digital certificate hierarchy*. 
	* For Organization Policies, their canonical path is usually "/Channel/<Application|Orderer>/<OrgName>/<PolicyName>".
	
	
### Certificate Authority CA ###
	* Is used to dispense X.509 digital certificates which acts as a identities to the administrators, network nodes, etc... 
	* Can also be used to sign transactions.
	* It has a built-in CA called *Fabric-CA*.
	* Fabric CA is a Private Root CA Provider capable of managing digital identities of Fabric participants that have the form of X.509 certificates. 
	* Fabric CA is a custom CA *targeting the Root CA needs* of Fabric, it is *Inherently Not Capable of Providing SSL Certificates* for general/automatic use in browsers.
	* CA gives digital certificate to requesting user of respective organization by signing the certificate with CAs` *Private Key* so that requested user can be sure that it hasn’t been tampered by verifying with the *Public Key* of CA.
	* One or More CAs can be used to define the members of an organization’s from a digital perspective.
	* CAs come in two flavors: Root CAs and Intermediate CAs.
	* Intermediate CAs have their certificates issued by the Root CA or another intermediate authority, allowing the establishment of a “Chain Of Trust” for any certificate that is issued by any CA in the chain. 
	* Chain Of Trust provides ability to track back to the Root CA not only allows the function of CAs to *Scale* while still providing *Security*. 
	* when a User is registered with a Fabric CA, a *Role* of admin, peer, client, orderer, or member must be associated with the user.
	* When a CA issues X.509 certificates, the *OU field (Manufacturing,Distribution)* in the certificate *Specifies the Line of Business* to which the *identity belongs*. 
	
	
	
### Applications ###
	* Applications can connect to both peers and orderers by using the channel with the help of SDK`s.
	* Single application of one organization can connect to one or more channels as per respective channel config in a network.
	* Organisations maintain the client applications.
	* X.509 certificates are used in client application (transaction proposals). 
	* Client application will have an identity that associates it with an organization.
	* Client application can invoke smart contracts, Once the chaincode definition has been committed to the channel.
	* Client applications send transaction proposals (serves as input to the smart contract) to peers owned by an organization specified by the smart contract endorsement policy, which uses it to generate an endorsed transaction response, which is returned by the peer node to the client application. (process called as Smart Contract Invocation).
	* When Fabric SDK is used to *register* a user with the CA, *Node OU Roles(client,peer,orderer,admin) & OU Attributes* are assigned to an *registering identity* which gains a appropriate special role to the identity. (SPECIAL CASE SCENARIO)
	* It is recommended that when the user is registered with the CA, that the *admin role in Node OU* is used to designate the node administrator. Then, the identity is recognized as an *Admin of ORG* by the Node OU role value in their signcert(certificate). As a reminder, in order to leverage the admin role, the “identity classification” feature must be enabled in the config.yaml above by setting “Node OUs” to Enable: true.
	* Applications receive Events asynchronously when Smart Contract Invocation process is complete.
	* Applications can, however, connect to one or more peers to issue a query.
	* Applications can register for different events(block,transaction,chaincode) so that they can be notified when they occur.
	* Event notifications conclude the third and final phase of the transaction workflow.
	* An application program can invoke a smart contract which uses simple ledger APIs to *get, put and delete* ledger states.
	
	
	
### Channels ###
	* Application channels are used to provide a private communication mechanism between organizations in the consortium.
	* Only network administrators (organization(s)) as defined in network configuration policy, can able to create new channel.
	* Channels keep *Transactions* private from the broader network.
	* Channels can serve for one or more applications.
	* Channel must have atleast one orderer to order trasactions.
	* Any updates to network configuration after creation of channels will have no direct effect on channel configuration.
	* Participants on a Fabric network establish a sub-network where every member has visibility to a particular set of transactions.
	* Only those nodes that participate in a channel have access to the smart contract (chaincode) and data transacted, preserving the privacy and confidentiality of both.
	* Allowing a group of participants to create a separate ledger of transactions.
	* Data in a channel is completely isolated from the rest of the network, including other channels.
	* One Ledger per Channel.
	* Above point means a completely separate blockchain, and completely separate world states, including namespaces.
	* There can be multiple channels in a network.
	* Channel can have any number of organizations connected to it.
	* Channel’s ledger contains a configuration block defining policies, access control lists, and other pertinent information.
	* Contain Membership Service Provider instances allowing for crypto materials to be derived from different certificate authorities.
	* Every channel runs on a *separate* instance of the Raft protocol, which allows each instance to elect a different leader.
	* Channel creators (and channel admins) have the ability to pick a subset of the available orderers and to add or remove ordering nodes as needed (as long as only a single node is added or removed at a time).
	
	
	
	
	
### Private Data Collection ###
	* Collections keep *Data* private between subsets of organizations on the channel.
	* Is used to segregate the data in a private database, logically separate from the channel ledger, accessible only to the authorized subset of organizations.
	* It is a collection (like DB) between members on a channel, allowing much of the same protection as channels without the maintenance overhead of creating and maintaining a separate channel.
	
	
	
	
### To Transact on a Fabric Network, ###
	* To Transact on a Fabric Network, a member( or anyone ) needs to:
		1)Have an identity issued by a CA that is trusted by the network.
		2)Become a member of an *Organization* that is recognized and approved by the network members. The MSP is how the identity is linked to the membership of an organization. Membership is achieved by adding the member’s public key (also known as certificate, signing cert, or signcert) to the organization’s MSP.
		3)Add the MSP to either a *Consortium* on the network or a channel.
		4)Ensure the MSP is included in the *Policy Definitions* on the network.
	
	
	
### New Oranization(s) coming inside the Channel are *allowed* by viewing their Channel MSP. 
### Channel MSP must *already* includes the MSP of a new organization to be joined in a channel.
### Above all detail must be included in a *Channel Configuration* of a channel or in a Consortium of network.
### So Channel Configuration has Channel MSP Details.

### Channel MSP defines *who* can come inside the channel but ***Channel Configuration Policy*** defines *what* operations can be done inside the channel who came through Channel MSP.



	
### Membership Service Provider MSP ###
	* For an identity to be *Verifiable* across the fabric network, it must come from a *Trusted Authority (MSP)*.
	* MSP is a component that defines the rules that govern the *Valid Identities* for every organization. 
	* MSPs turn *Verifiable Identities* into the *Members* of a blockchain network.
	* Mapping of X.509 digital certificates to member organizations is achieved by via a structure called a (MSP).
	* Members of a Hyperledger Fabric network enroll through a trusted MSP.
	* Default MSP implementation in Hyperledger Fabric Network uses X.509 certificates as identities, adopting a traditional Public Key Infrastructure (PKI) hierarchical model. 
	* PKI certificate authorities provides a list of identities, and an MSP says which of these are members of a given organization that participates in the network.
	* Implementation of the MSP requirement is a set of folders that are added to the configuration of the network.
	* MSP is used to define an organization both *Inwardly* (organizations decide who its admins are) and *Outwardly* (by allowing other organizations to validate that entities have the authority to do what they are attempting to do).
	* MSP identifies which Root CAs and Intermediate CAs are accepted to define the members of a trust domain by *Listing the Identities of their members*, or by identifying which CAs are authorized to issue valid identities for their members.
	* MSP defines Admin of the Organization, the Admin of the Node, and the Node itself should all have the same root of trust.
	* MSPs occur in Two Domains in a blockchain network:
		* Local MSP - Locally on an actor’s node			
		* Channel MSP - In channel configuration
			
	
	
	
### Local MSP ###
	* Local MSP defines who has administrative or participatory rights at that level. 
	* Local MSPs defines Permissions for clients and for nodes (peers and orderers).
	* Every Node and Every Orderer must have a Local MSP defined separately.
#	* Every Organization  have a Single MSP( includes both Node & Orderer Local MSP) to list the actors or nodes it trusts.
	1) Node Local MSP:
		* Define the permissions for a Node (who are the peer admins who can operate the node).
		* Node Local MSPs are represented as a *Folder Structure* on the *File System* (includes Node & User).
		* Physically and Logically, there is only one local MSP per node.
		* Peer Admins will not necessarily be Channel Admins, and vice versa.
		* The local MSPs of Clients (the account holders in the banking scenario above), allow the user to authenticate itself in its transactions as a member of a channel (e.g. in chaincode transactions), or as the owner of a specific role into the system such as an organization admin, for example, in configuration transactions.
		* This(Node Local MSP) allows for authenticating member messages *Outside the Context of a Channel* and to define the permissions over a particular node (who has the ability to install chaincode on a peer, for example). 
	2) Orderer Local MSP:
		* Defined on the *File System* of the orderer node and only applies to that orderer node.
		* Physically and Logically, there is only one local MSP per node.
	
	
		
### Application Channel MSP ###
	* Channel MSPs contain the MSPs of the organizations of the *Channel Members* (including Orderer of channel).
	* Channel MSPs define administrative and participatory rights at the Channel Level.
	* Defines the *Relationship* between the identities of channel members (which themselves are MSPs) and the enforcement of channel level policies.
	* Channel MSPs identify who has *Authorities* at a channel level.
	* Channel MSPs are described in a *Channel Configuration*.
	* As channel MSPs are available to all nodes in the channel,they are *Logically defined Once* in the channel configuration.
	* Instantiated on the file system of every node in the channel and kept synchronized via consensus.
	* Peers and Ordering Nodes on an application channel share the *Same View* of channel MSPs.
	* While there is a copy of each channel MSP on the local file system of every node (of which they are a member), logically a channel MSP resides on and is maintained by the *Channel or the Network*.
	* If an organization wishes to join the channel, an MSP incorporating the chain of trust for the organization’s members would need to be included in the channel configuration.
	* Channel MSP configuration does not include *Keystore & Signcerts* folder(private & public key), because channel MSPs solely aim to offer Identity Validation Functionalities and not signing abilities.
	* Channel MSP includes the Revoked Certificates (This list is conceptually the same as a CA’s Certificate Revocation List (CRL), but it also relates to *revocation of membership* from the organization.)
	
	
	

### System Channel MSP ###
	* Includes the MSPs of all the organizations that *Participate* in an Ordering Service.
	
	
### Assets ###
	* Can be tangible (real estate and hardware)
	* Can also be intangible (contracts and intellectual property)
	* Assets can be modified using chaincode transactions.
	* Represented as a collection of key-value pairs.
	* With state changes recorded as transactions on a Channel ledger.
	* Can be represented in binary and/or JSON form.
	
	
	
	
### Ordering Service ###
	* Ordering Service will likely include *Ordering Nodes* from multiple organizaitons and *Collectively* these organizations run the ordering service, most importantly managing the *Consortium of Organizations* and the default policies that are inherited by the application channels.
	* Fabric’s design for ordering service relies on *Deterministic* consensus algorithms not a probablistic one (done in permissionless blockchains), any block validated by the peer is guaranteed to be final and correct.
	* Currently offering a CFT ordering service implementation based on the *etcd* library of the Raft protocol.
	* Network can have multiple ordering services (like CFT or BFT in same n/w) supporting different applications or application requirements. (Note this point: which is different from multiple orderer organizations having orderers like CFT1,CFT2,etc for a single ordering service like CFT for a single application requirements.)
	*Every channel runs on a separate instance of the Raft protocol, which allows each instance to elect a different leader among many ordering nodes in a single (application)channel.VERY IMPORTANT --- In Multiple ordering service cluster (each cluster for one application channel) While all Raft nodes (may be a leader ordering node or all in each application channel) must be part of the system channel, they do not necessarily have to be part of ***all*** application channels. Each application channels running a one single cluster of many ordering nodes electing a leader ordering node (may be raft node).
	
	
	
### Consortium ###
	* Consortium defines the *Set of Organizations* in the network who share a need to *Transact* with one another.
	* It really makes sense to group organizations together as a single consortium if they have a common goal,
	* Can have any number of organizational members.
	* Only network administrators (organization(s)) as defined in network configuration, can able to create new consortia.
	* While creating the consortium or the channel, the relevant administrators of channel set the policies that who is authorized to modify a configuration element in a channel.
	* Every consortium has a single channel for their organizational members in a consortium.
	* Consortium definition, by network administrator, is stored in the network configuration.
	
	
	
### Declarative Policies ###
	* How organizations manage network evolution.
	
	
### Chaincode Definition ###
	* A set of parameters that establish how a chaincode will be used on a channel.
	* It has endorsement policy for a smart contract ( describes which organizations` peer should digitally sign a generated transaction(not a chaincode) before they will be accepted by other organizations(committing peer’s) onto their copy ofthe ledger).
	* Committing the chaincode definition to the channel, places the endorsement policy on the channel ledger.



### Fabric Network Governance ###
	* Network is governed according to policy rules specified in *Network Configuration*.
	* Newtork can be controlled by one or more organizations.
	
	
	
### Network Configuration (policy) ###
	* Defines the configuration settings for the orderer.
	* Defines consortium definition.
	* N/W Config. policy can be considered more important than Orderers because, ultimately, it controls network access.
	* It gives administrative rights to organization.
	* It contains the policies that describe the starting set of administrative capabilities for the network.
	* It may change later due to addition or removal of the members of the fabric network.
	* List of Organizations (Consortium) is kept in the configuration of the “ordering system channel” that are allowed to create Channels.
	* If consortia definition is changed in n/w configuration, it will not affect the members of channel after creation of channels.
	* Policy which separates organizations that can manage resources at the network level.
	* Channel configurations remain completely separate from each other, and completely separate from the network configuration
	* Each node in the ordering service records each channel in the network configuration, so that there is a record of each channel created, at the network level.
	* Although ordering service node creates consortia and channels, the *Intelligence* of the network is contained in the *Network Configuration* that Ordering services(orderers) is obeying.
	
	
	
### Application Channel Governance ###
	* Channel is governed according to the *Policy Rules* specified in *Channel Configuration*.
	* Channel (channel configuration) can be controlled by one or more organizations (org`	s peers, must be member of the channel).
	* Channel configuration determines which & how many peers in channel can read and/or write information to channel ledger.
	* Administrating organization(s) has *No Rights* in channel configuration.
	* Administrating organization(s) cannot add itself to the *Channel*, must be authorized by channel members as per channel configuration.
	* Anchor peers for one org. in a channel are defined in the channel configuration for that organization(communicating org. or from org.).
	* Organization(s) who can manage resources at the channel level.
	* Number of transactions in a block depends on channel configuration parameters related to the desired size and maximum elapsed duration for a block (BatchSize and BatchTimeout parameters, to be exact).
	
	
	
	
### Modification Policy or mod_policy ###
	* Is a first class policy within a network or channel configuration that manages change. 
	* The key point of understanding is that policy change in a network or channel configuration is managed by a policy (mod_policy) within the respective policy itself.
	* A uniquely powerful policy that allows network and channel administrators to manage policy change itself.
	* Mod_Policy defines a set of organizations that are allowed to change the mod_policy itself.
	* Organization(s) defined in the mod_policy inside n/w configuration policy is responsible for *Configuration Changes*
	* Mod_Policy can be configured in such a way that all organization defined in mod_policy would have to approve the change.
	* Note that separate mod_policy for both n/w & channel configuration policies within the policies respectively. 
	
	


### (N/W & Channel) Configuration Transactions ###
	* Network Configuration Transaction:
		* To change a network configuration, a network administrator must submit a *Configuration Transaction* to change the network configuration.
		* It must be signed by the organizations identified in the *Mod_Policy* (with network configuration) as being responsible for network configuration change.
		* WKT, ordering service nodes (multiple orderers) are connected via the *System Channel*.
		* Using the system channel, ordering service nodes distribute *Network Configuration Transactions*.
		* These transactions are used to co-operatively maintain a consistent copy of the *Network Configuration at Each Ordering Service Node*.
		
	* Channel Configuration Transactions:
		* To change a channel configuration, a channel administrator must submit a *Configuration Transaction* to change the channel configuration.
		* It must be signed by the organizations identified in the *Mod_Policy* (with channel configuration) as being responsible for channel configuration change.
		* Channel configuration transactions are processed by the orderer, as it needs to know the current set of policies to execute its basic form of access control.
		* In a similar way, peer nodes in an *Application Channel* can distribute channel configuration transactions.
		* These transactions are used to maintain a consistent copy of the *Channel Configuration at Each Peer Node*.
		
	* Every configuration change results in a new configuration block transaction being generated.
	
	
	
	
### Policy ###
	* Policy is a set of rules that define the structure for how decisions are made and specific outcomes are reached.
	* Policies typically describe **Who** and a **What**, such as the access or rights that an individual has over an *Asset*.
	* Everything you want to do on a Fabric network is controlled by a *Policy*.
	* Policies are agreed to by the consortium members when a network is originally configured, but they can also be modified as the network evolves. For example, they describe the criteria for adding or removing members from a channel, change how blocks are formed, or specify the number of organizations required to endorse a smart contract.
	* Each policy has a **Type** which describes how the policy is expressed (Signature or ImplicitMeta) and a **Rule**.
	* Hyperledger Fabric Policy Hierarchy:
		1) System Channel         - Consortium Membership and blockchain structure
		2) Application Channel    - Transaction Networks and business logic
		3) ACLs & Smart Contracts - Transactions, data and events
		
		
		
### System & Application Channel Configuration & ACL ###
	* System Channel Configuration:
		* Every network begins with an ordering *System Channel*.
		* There must be exactly one ordering system channel for an ordering service.
		* It is the First Channel to be created.
		* The system channel also contains the organizations who are the members of the ordering service (ordering organizations) and those that are on the networks to transact (consortium organizations). 
		* The **Policies** in the ordering system channel configuration blocks govern the consensus used by the ordering service and define how new blocks are created.
		* The system channel also governs which members of the consortium are allowed to create new channels.
	* Application Channel Configuraton:
		* The **Policies** in an application channel govern the ability to add or remove members from the channel.
		* Application channels also govern which organizations are required to approve a chaincode before the chaincode is defined and committed to a channel using the Fabric chaincode lifecyle. 
		* When an application channel is initially created, it **Inherits** all the ordering service parameters from the orderer system channel by default.
		* However, those parameters (and the policies governing them) can be customized in each channel.
		* Channel Policies are defined in "configtx/configtx.yaml".
	* ACL`s
		* Provides the ability to configure *Access to Resources* by associating those resources with existing policies. 
		* “Resources” could be functions on system chaincode (e.g., “GetBlockByNumber” on the “qscc” system chaincode) or other resources (e.g.,who can receive Block events).
		* ACLs refer to policies defined in an application channel configuraton and extends them to control additional resources. 
		* The default set of Fabric ACLs is visible in the *configtx.yaml* file under *Application:&ApplicationDefaults* section but they can and should be overridden in a production environment.
		* The list of resources named in configtx.yaml is the complete set of all internal resources currently defined by Fabric.
	* Explicit & Implicit Sign:
		* Each policy has **Type** which describes how the policy is expressed (Signature or ImplicitMeta) and a **Rule**.
		* If you want to change anything in Fabric, the policy associated with the resource describes *who* needs to approve it, either with an *Explicit sign* off from Individuals, or an *Implicit sign* off by a Group. 
		* Explicit sign offs in policies are expressed using the *Signature* syntax and implicit sign offs use the *ImplicitMeta* syntax.
		* This (ImplicitMeta Syntax) is particularly useful because the members of that group can change over time without requiring that the policy be updated.
		* Signature Policy:
			* Signature policies define specific types of users who must sign in order for a policy to be satisfie such as Org1.Peer OR Org2.Peer. 
			*  The syntax supports arbitrary combinations of *AND, OR and NOutOf*.
		* ImplicitMeta Policy:
			* ImplicitMeta policies are only valid in the context of channel configuration which is based on a tiered hierarchy of policies in a configuration tree.
			* Key benefit of an ImplicitMeta policy such as **MAJORITY Admins** is that when you add a new admin organization to the channel, you do not have to update the channel policy.
			* ImplicitMeta policies are considered to be more flexible as the consortium members change.
			* The *Consortium on the Orderer* can change as new members are added or an existing member leaves with the consortium members agreeing to the changes, but no policy updates are required.
			* Recall that ImplicitMeta policies ultimately resolve the Signature sub-policies underneath them in the configuration tree. 
			* *Always*, ImplicitMeta policies (Reader, Writer, and Admin ImplicitMeta policies) point to sub-policies (Reader, Writer, and Admin) defined for each organization.
	
	
	
### Fabric Policy Governance ###
	* System Channel:
		1) What Orderer Organizations Governs:
			* Blockchain Network Structure
			* Consensus
			* Consortium Membership
			* Consortium Member Policies policies (Readers, Writers, Admins)
		2) What Consortium Organizations Governs:
			* Channel Modification
			
	* Application Channel:
		1) What Orderer Organizations Governs:
			* Consensus
		2) What Consortium Organizations Governs:
			* Channel Membership
			* Organization Policies (Readers, Writers, Admins)
			
	* ACLs and Smart Contracts:
		1) What Orderer Organizations Governs:
			* Nothing
		2) What Consortium Organizations Governs:
			* Smart contracts
			* Ledger Data
			* Events
			
			
			
			
### Overriding Policy Definitions ###
	* Hyperledger Fabric includes default policies which are useful for getting started, developing, and testing your blockchain, but they are meant to be customized in a production environment.
	* You should be aware of the default policies in the configtx.yaml file. 
	* Channel configuration policies can be extended with *Arbitrary Verbs*, beyond the default Readers, Writers, Admins Policies in configtx.yaml.
	* The orderer system and application channels are overridden by issuing a config update when you override the default policies by editing the configtx.yaml for the orderer system channel or the configtx.yaml for a specific channel.
	
		
	
	
### Identity ###
	* It determines the exact permissions over resources and access to information that actors have in a blockchain network.
	* Digital Identity === Identity + Principal
	* Principals include properties of an actor’s identity, such as the actor’s organization, organizational unit, role or even the actor’s specific identity.



### Gossip Protocol ###
	* The technical mechanism by which peers within an individual organization efficiently discover and communicate with each other when an organization have large number of peer nodes.
	* Not every peer needs to be connected to an orderer — *peers can cascade blocks to other peers using the gossip protocol*, who also can process them independently (blocks). 

###################################################################################################





