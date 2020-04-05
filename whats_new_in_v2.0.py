#################################################     *What's New in v2.0*     ####################
### Decentralized Governance for Smart Contracts ###
	* New Fabric chaincode lifecycle allows multiple organizations to come to agreement on the parameters of a chaincode, such as the chaincode endorsement policy, before it can be used to interact with the ledger.
	* It supports both centralized trust models (in v1.x previous lifecycle model) as well as decentralized models (in v2.0).
	* New model allows for a chaincode to be upgraded only after sufficient number of organizations have approved theupgrade.
	* Fabric lifecycle allows you to change an endorsement policy or private data collection configuration without having to repackage or reinstall the chaincode. 
	* You can now use a single chaincode package and deploy it multiple times with different names on the same channel or on different channels.
	* Chaincode packages do not need to be identical across channel members.
	
	
	
### Private Data Enhancements ###
	* Private data collections can now optionally be defined with an endorsement policy that overrides the chaincode-level endorsement policy for keys within the collection.
	
	
	
### External Chaincode Launcher ###
	* Chaincode is no longer required to be run in Docker containers, and may be executed in the operator’s choice of environment (including containers or  in a Kubernetes pod).
	* Now possible to run *Chaincode As an External Service*, for example in a Kubernetes pod, which a peer can connect to and utilize for chaincode execution.
	* *External Chaincode Launcher Feature* -- An operator can provide a set of external builder executables to override how the peer builds and launches chaincode.
	
	
	
### Alpine-based Docker Images ###
	* Starting with v2.0, Hyperledger Fabric Docker images will use Alpine Linux, a security-oriented, lightweight Linux distribution.
	
	
	
### Upgrading to Fabric v2.0 ###
	* Rolling upgrades from v1.4.x to v2.0 are supported, so that network components can be upgraded one at a time with no downtime.
	
	
	
### Comparison of Chaincode Lifecycle b/w v1.x & v2.0 ###
	* In v1.x versions of Fabric, one organization had the ability to set parameters of a chaincode (for instance the endorsement policy) for all other channel members, who only had the power to refuse to install the chaincode and therefore not take part in transactions invoking it. 
	* In 2.0, it supports both centralized trust models (in v1.x previous lifecycle model) as well as decentralized models (in v2.0) requiring a sufficient number of organizations to agree on an endorsement policy and other details before the chaincode becomes active on a channel.

###################################################################################################








