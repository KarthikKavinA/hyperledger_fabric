#################################################     *Justification*     #########################
### Confidentiality in Fabric N/W ###
	* One approach    - Encrypting Data -- Given enough time and computational resource, the encryption could be broken.
	* Second approach - Zero Knowledge Proofs (ZKP) -- Computing a ZKP requires considerable time and computational resources. Hence, the trade-off in this case is performance.
	* Both approaches have their trade-offs. So, Channels and Private Data Collections are used.
	
	
### Scalability and Confidentiality ###
	* Endorsing Nodes keeps the logic of the chaincode confidential to endorsing organizations. This is in contrast to the output of the chaincodes (the transaction proposal responses) which are shared with every peer in the channel, whether or not they endorsed the transaction. 
	* This specialization of endorsing peers is designed to help scalability and confidentiality.
	
	
### Encryption of Transactions ###
	* To further obfuscate the data, values within chaincode can be encrypted (in part or in total) using common cryptographic algorithms such as AES before sending transactions to the ordering service and appending blocks to the ledger. Once encrypted data has been written to the ledger, it can be decrypted only by a user in possession of the corresponding key that was used to generate the cipher text.
	
### Separation & collaboration b/w organizations ###
	* This is a very powerful concept – Channels provide both a mechanism for the separation of organizations, and a mechanism for collaboration between organizations. All the while, this infrastructure is provided by, and shared between, a set of independent organizations.
	
	
### Need For Organizational Units ###
	* When a CA issues X.509 certificates, the *OU field (Manufacturing,Distribution)* in the certificate *Specifies the Line of Business* to which the *identity belongs*.
	* A benefit of using OUs like this is that these values can then be used in policy definitions in order to restrict access or in smart contracts for attribute-based access control.
	* Otherwise, separate MSPs would need to be created for each organization.
	
	

### Speciality of Node OU Roles ###
	* Special kind of OU called Node OU, that can be used to confer(provide) a role onto an identity.
	* This is particularly useful when you want to restrict the members of an organization to the ones holding an identity (signed by one of MSP designated CAs) with a specific Node OU role in it. 
	* For example, with node OU’s you can implement a more granular endorsement policy that requires Org1 peers to endorse a transaction, rather than any member of Org1.
	
	
	
### Importance of Channel Config. Policy , (Eventhough Coming Identity has Admin rights defined in Channel MSP) --- No Power ###
	* For Channel MSPs, just because an actor has the role of an administrator it doesn’t mean that they can administer particular resources. The actual power a given identity has with respect to administering the system is determined by the ***policies*** that manage system resources. For example, a channel policy might specify that ORG1-MANUFACTURING administrators, meaning identities with a ***role of Admin*** and a ***Node OU of ORG1-MANUFACTURING*** (both must be viewed to add an org), have the rights to add new organizations to the channel, whereas ORG1-DISTRIBUTION administrators have no such rights (because *Node OU of ORG1-DISTRIBUTION* is different).
	* It is recommended that when the user is registered with the CA, that the *admin role in Node OU* is used to designate the node administrator. Then, the identity is recognized as an *Admin of ORG* by the Node OU role value in their signcert(certificate). As a reminder, in order to leverage the admin role, the “identity classification” feature must be enabled in the config.yaml above by setting “Node OUs” to Enable: true.
	
	
	
### Careful Usage of OUs ###
	* Finally, OUs could be used by different organizations in a consortium to distinguish each other. But in such cases, the different organizations have to use the same Root CAs and Intermediate CAs for their chain of trust, and assign the OU field to identify members of each organization. When every organization has the same CA or chain of trust, this makes the system more centralized than what might be desirable and therefore deserves careful consideration on a blockchain 	  network.
	

	
	
### D/B Channel and Private Data Collections ###
	* Channels keep *Transactions* private from the broader network whereas Collections keep *Data* private between subsets of organizations on the channel.
	
### Systems of Proof ###
	* In addition to being decentralized and collaborative, the information recorded to a blockchain is append-only, using cryptographic techniques that guarantee that once a transaction has been added to the ledger it cannot be modified. This property of “Immutability” makes it simple to determine the provenance of information because participants can be sure information has not been changed after the fact. It’s why blockchains are sometimes described as Systems Of Proof.
	
	
### Strict Ordering of Transactions ###
	* It’s worth noting that the sequencing of transactions in a block is not necessarily the same as the order received by the ordering service, since there can be multiple ordering service nodes that receive transactions at approximately the same time. What’s important is that the ordering service puts the transactions into a strict order, and peers will use this order when validating and committing transactions.
	* This strict ordering of transactions within blocks makes Hyperledger Fabric a little different from other blockchains where the same transaction can be packaged into multiple different blocks that compete to form a chain.
	
	
	
### Ledger Immutability & Finality ###
	* In Hyperledger Fabric, the blocks generated by the ordering service are *Final*. Once a transaction has been written to a block, its position in the ledger is immutably assured. As we said earlier, Hyperledger Fabric’s finality means that there are *No Ledger Forks* — validated transactions will never be reverted or dropped.
	
	
	
### Disadvantages in Multi-cluster Ordering Service ###
	* Every channel runs on a separate instance of the Raft protocol, which allows each instance to elect a different leader.
	* This configuration also allows further decentralization of the service in use cases where clusters are made up of ordering nodes controlled by different organizations.
	* But, While this configuration creates more overhead in the form of redundant heartbeat messages and goroutines, it lays necessary groundwork for BFT.

	


### Final Version Check (i.e., Committing phase) - Double Spend Problem ###
	* Final Version Check by peers in committing phase provides protection against *Double Spend Operations* and other threats that might compromise data integrity, and allows for functions to be executed against non-static variables.


### De-centralized Network ###
	* The careful use of network and channel policies allow even large networks to be well-governed. Organizations are free to add peer nodes to the network so long as they conform to the policies agreed by the network. *Network and Channel Policies* create the balance between *Autonomy and Control* which characterizes a De-Centralized Network.
	* Objects like network configurations, that are logically single, turn out to be physically replicated among a set of ordering services nodes. channel configurations, ledgers, and to some extent smart contracts which are installed in multiple places but whose interfaces exist logically at the channel level. It enables Hyperledger Fabric Blockchain Network to be both *DeCentralized* and yet *Manageable* at the same time. 
	* Every channel runs on a separate instance of the Raft protocol, which allows each instance to elect a different leader. This configuration also allows further decentralization of the service in use cases where clusters are made up of ordering nodes controlled by different organizations.
	


###################################################################################################








