################################################# *Extended Topics* ###############################
### System channel & Application Channel ###
	* Both network and channel configurations are kept consistent using the same blockchain technology that is used for user transactions – but for configuration transactions. To change a network or channel configuration, an administrator must submit a configuration transaction to change the network or channel configuration. It must be signed by organizations identified in the appropriate policy as being responsible for configuration change. This policy is called the mod_policy and we’ll discuss it later.
	* Indeed, the ordering service nodes operate a mini-blockchain, connected via the system channel we mentioned earlier. Using the system channel ordering service nodes distribute network configuration transactions. These transactions are used to co-operatively maintain a consistent copy of the network configuration at each ordering service node. In a similar way, peer nodes in an application channel can distribute channel configuration transactions. Likewise, these transactions are used to maintain a consistent copy of the channel configuration at each peer node.
	
	
	
### Importance of Consensus ###
	* Consensus is not merely limited to the agreed upon order of a batch of transactions; rather, it is an overarching characterization that is achieved as a byproduct of the ongoing verifications that take place during a transaction’s journey from proposal to commitment.
	
	
### Formation of Blockchain Network ###
	* In most cases, multiple organizations come together as a consortium to form the network and their permissions are determined by a set of policies that are agreed by the consortium when the network is originally configured. Moreover, network policies can change over time subject to the agreement of the organizations in the consortium, as we’ll discover when we discuss the concept of modification policy.
	
	
### careful addition of peers ###
	* More peers in a network will allow more applications to connect to it; and multiple peers in an organization will provide extra resilience in the case of planned or unplanned outages.
	
	
### Types of peers ###
	* These are the two major types of peer:
		1)Committing Peer = Every peer node in a channel is a committing peer. It receives blocks of generated transactions, which are subsequently validated before they are committed to the peer node’s copy of the ledger as an append operation.
		2)Endorsing Peer = Every peer with a smart contract can be an endorsing peer if it has a smart contract installed. However, to actually be an endorsing peer, the smart contract on the peer must be used by a client application to generate a digitally signed transaction response. The term endorsing peer is an explicit reference to this fact.
	* There are two other roles a peer can adopt:
		1)Leader peer = When an organization has multiple peers in a channel, a leader peer is a node which takes responsibility for distributing transactions from the orderer to the other committing peers in the organization. A peer can choose to participate in static or dynamic leadership selection.
		2)Anchor Peer = If a peer needs to communicate with a peer in another organization, then it can use one of the anchor peers defined in the channel configuration for that organization. An organization can have zero or more anchor peers defined for it, and an anchor peer can help with many different cross-organization communication scenarios.
		
		
		
### Leadership Selection for Leader Peer ###
	* A peer can choose to participate in static or dynamic leadership selection.
	* It is helpful, therefore to think of two sets of peers from leadership perspective – those that have static leader selection, and those with dynamic leader selection. For the static set, zero or more peers can be configured as leaders. For the dynamic set, one peer will be elected leader by the set. Moreover, in the dynamic set, if a leader peer fails, then the remaining peers will re-elect a leader.
	* It means that an organization’s peers can have one or more leaders connected to the ordering service. This can help to improve resilience and scalability in large networks which process high volumes of transactions.
	
	
### Issuing Digital Certificates --- CA ###
	* A Certificate Authority dispenses certificates to different actors.These certificates are digitally signed by the CA and bind together the actor with the actor’s public key (and optionally with a comprehensive list of properties). As a result, if one trusts the CA (and knows its public key), it can trust that the specific actor is bound to the public key included in the certificate, and owns the included attributes, by validating the CA’s signature on the actor’s 		  certificate.
	
	
### Node OU Roles ###
	* Special kind of OU called Node OU, that can be used to confer(provide) a role onto an identity.
	* These Node OU roles are defined in the **$FABRIC_CFG_PATH/msp/config.yaml** file.
	* Contain a list of organizational units whose members are considered to be part of organization represented by this MSP.  
	* This is particularly useful when you want to restrict the members of an organization to the ones holding an identity (signed by one of MSP designated CAs) with a specific Node OU role in it. For example, with node OU’s you can implement a more granular endorsement policy that requires Org1 peers to endorse a transaction, rather than any member of Org1.
	* In order to use the Node OU roles, the “identity classification” feature must be enabled for the network. When using the folder-based MSP structure, this is accomplished by enabling “Node OUs” in the config.yaml file which resides in the root of the MSP folder.
	* There are 4 possible Node OU ROLES for the MSP:
		* client, peer, admin, orderer
		* you no longer have to explicitly place *certs* in the *admincerts* folder of the MSP directory. Rather, the *admin role* present in the user’s signcert qualifies the *identity* as an *admin user*.


### Determinism --- Smart Contracts ###
	* Smart contracts executing in a blockchain that operates with the order-execute architecture must be deterministic; otherwise, consensus might never be reached. To address the non-determinism issue, many platforms require that the smart contracts be written in a non-standard, or domain-specific language (such as Solidity) so that non-deterministic operations can be eliminated. This hinders wide-spread adoption because it requires developers writing smart contracts to learn a new language and may lead to programming errors.
	
	
	
### Non - determinism ###
	* For the same transaction proposal, different peers can return different results and therefore inconsistent transaction responses to the application because the chaincode is non-deterministic. Non-determinism is the enemy of chaincodes and ledgers and if it occurs it indicates a serious problem with the proposed transaction, as inconsistent results cannot, obviously, be applied to ledgers. An individual peer cannot know that their transaction result is non-deterministic — transaction responses must be gathered together for comparison before non-determinism can be detected.
	
	
	
	
### Decentralized Agreement --- Smart Contracts ###
	* Human decisions can be modeled into a chaincode process that spans multiple transactions. The chaincode may require actors from various organizations to indicate their terms and conditions of agreement in a ledger transaction. Then, a final chaincode proposal can verify that the conditions from all the individual transactors are met, and “settle” the business transaction with finality across all channel members. For a concrete example of indicating terms and conditions in private, see the asset transfer scenario in the Private data documentation.
	
	
### Permissionless Blockchain ###
	* Open permissionless system that allows unknown identities to participate in the network (requiring protocols like “proof of work” to validate transactions and secure the network), 
	
	
### Consensus - Practical Byzantine Fault Tolerance ###
	* PBFT can provide a mechanism for file replicas to communicate with each other to keep each copy consistent, even in the event of corruption. Alternatively, in Bitcoin, ordering happens through a process called mining where competing computers race to solve a cryptographic puzzle which defines the order that all processes subsequently build upon.
	
	
### Private Data Collections ###
	* When a subset of organizations on that channel need to keep their transaction data confidential, a private data collection (collection) is used to segregate this data in a private database, logically separate from the channel ledger, accessible only to the authorized subset of organizations.
	
	
### MSP -- should be cleared ###
	* Network configuration NC4 uses a named MSP to identify the properties of certificates dispensed by CA4 which associate certificate holders with organization R4. NC4 can then use this MSP name in policies to grant actors from R4 particular rights over network resources. An example of such a policy is to identify the administrators in R4 who can add new member organizations to the network. We don’t show MSPs on these diagrams, as they would just clutter them up, but they are very important.
	
	
### PKI ###
	* A PKI is comprised of Certificate Authorities who issue digital certificates to parties (e.g., users of a service, service provider), who then use them to authenticate themselves in the messages they exchange in their environment. A 	  CA’s Certificate Revocation List (CRL) constitutes a reference for the certificates that are no longer valid. Revocation of a certificate can happen for a number of reasons. For example, a certificate may be revoked because the cryptographic private material associated to the certificate has been exposed.
	* There are four key elements to PKI:
		* Digital Certificates
			* A digital certificate is a document which holds a set of attributes relating to the holder of the certificate.
			* The most common type of certificate is the one compliant with the X.509 standard, which allows the encoding of a party’s identifying details in its structure.
			* Digital Certificate has Public Key whereas Private Key must be kept private.
		* Public and Private Keys
			* Public Key that is made widely available and acts as Authentication Anchor.
			* Private Key that is used to produce Digital Signatures on messages.
			* Recipients of digitally signed messages (using Private Key) can verify the Origin and Integrity of a received message by checking that the attached signature is valid under the *Public Key* of the expected sender.
		* Certificate Authorities
			* One or More CAs can be used to define the members of an organization’s from a digital perspective.
		* Certificate Revocation Lists
			* It’s just a list of references to certificates that a CA knows to be revoked for one reason or another.
			* When a third party(one org.) wants to verify another(other org.) party’s identity, it first checks the issuing CA’s CRL to make sure that the certificate has not been revoked. A verifier doesn’t have to check the CRL, but if they don’t they run the risk of accepting a compromised identity.
			* Using a CRL to check that a certificate is still valid. If an impersonator tries to pass a compromised digital certificate to a validating party, it can be first checked against the issuing CA’s CRL to make sure it’s not listed as no longer valid.
###################################################################################################	


































