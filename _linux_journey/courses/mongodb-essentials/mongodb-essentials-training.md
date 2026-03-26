---
title: "Mongodb Essentials Training"
category: "mongodb-essentials"
tags: ["mongodb-essentials", "mongodb", "essentials", "training"]
---

* MongoDB first released in 2009.
* MongoDB built with distribution in mind.
* Open Source.
* MongoDB has implemented the following features:
	* Schema validation.
	* ACID compliance
	* Joins
* MongoDB uses sharding.
	* Can re-shard on command.
* Client-Side Field-Level Encryption.
* Data is never unencrypted.
* If deploy MongoDB in cloud, have to check MongoDB Connection String
* Regardless of install option, need the following:
	* MongoDB
	*  MongoDB Shell
	* MongoDB Database Tools
* MongoDB Community
* MongoDB Enterprise
	* Advanced security options.
	* storage engines.
	* Management tools.
	* MongoDB Enterprise Kubernetes Operator
	* MongoDB Connector for BI
* mongod
	* daemon process MongoDB
	* handles requests from MongoDB shell or drivers
	* performs background management operations
* Mongo listens by default on Port 27017
	* /data/db in Linux
	* C:\data\db*
* To insert a value, run this command:
`db.test.insertOne({"hello": "world"})`
* Production environments run one more than mongod process, due to fault tolerance 
* Replica Sets
	* Roles
	* One member is elected as the Primary.
	* Primary receives all write operations.
	* The other ones are Secondaries.
		* Replicate operations from the Primary asynchronously, maintain exact same data sets.
	* If a Primary becomes unavailable, election is held and Secondary takes over as new Primary.
		* More than half of the replica set members have to vote for the new Primary.
	* Have an uneven number of replica set members, so that a successful outcome can be reached.
* Setting up a Replica Set:
	* openssl rand -base64 755 > keyfile
		* Allows the running of MongoDB without authentication.
	* Generally it is recommended that X.509 certificate instead.
	* Make sure only current user has read access with `chmod 400`
	* Shell Parameter Extensions:
		* `mkdir -p m{1,2,3}/db`
	* `mongod --replSet myReplSet --dbpath ./m1/db --logpath ./m1/mongodb.log --port 27017 --keyFile ./keyfile`
	* `mongod --replSet myReplSet --dbpath ./m2/db --logpath ./m2/mongodb.log --port 27018 --fork --keyFile ./keyfile`
	* `mongod --replSet myReplSet --dbpath ./m3/db --logpath ./m3/mongodb.log --port 27019 --fork --keyFile ./keyfile`
	* Start the replication with:
		* `rs.initiate()`
	* To switch to the admin user, use the following command:
		* `use admin`
	* LocalHost Exception for creating a user.
		* This commands creates a user within the DB (need admin privileges) and prompts for a password:
			* `db.createUser({user: 'myuser', pwd: passwordPrompt(), roles: ["root"]})`
		* To then authenticate the user from the admin setting:
			* `db.getSiblingDB("admin").auth("myuser", passwordPrompt())`
		* Add each of the replica sets with this command:
			* ` rs.add("localhost:27017")`
			* `rs.add("localhost:27018")`
			* `rs.add("localhost:27019")`
		* Can check the status of the replica set with:
			* `rs.status`
			* `db.serverStatus()["repl"]`
			* Shows each of the members.
* `ctrl + d`
	* Exits Mongo.
* `killall mongod`
	* Kills all mongo running processes.
* Replica Set From a Configuration File
`MBP00-3f041b:replicaset $ openssl rand -base64 755 > keyfile
MBP00-3f041b:replicaset $ chmod 400 keyfile
MBP00-3f041b:replicaset $ mkdir -p m{1,2,3}/db
MBP00-3f041b:replicaset $ touch m1.conf
MBP00-3f041b:replicaset $ vim m1.conf
MBP00-3f041b:replicaset $ cp m1.conf m2.conf
MBP00-3f041b:replicaset $ cp m1.conf m3.conf
MBP00-3f041b:replicaset $ vim m2.conf
MBP00-3f041b:replicaset $ vim m3.conf
MBP00-3f041b:replicaset $ mongod -f m1.conf`
* To start the replica ste, run the `mongod -f m1.conf` command.
* To connect to one of the instances, we just run `mongosh`
* Right out the config variable
	* `use admin`
	* config = { _id: "mongodb-essentials-rs", members: [{_id: 0, host: "localhost:27017"}, {_id: 1, host: "localhost:27018"}, {_id: 2, host: "localhost:27019"}]}
	* rs.initiate(config)
	* How to initiate the replica set.
* Create User with Local Host Exception:
* The first user you create, should have privileges to create further users.
	* db.createUser({user: 'myuser', pwd: passwordPrompt(), roles: ["root"]})
* To authenticate, you have to authenticate again the database where you created the user.
	* db.getSiblingDB("admin").auth("myuser")
* rs.status()
	* Reports on the health of replica set members.
* db.serverStatus()['repl']
	* Gets the "repl" field value.
* MongoDB Database Tools
	* mongostat
		* Statistics on a running mongod
	* mongodump
		* Export dump files to BSON
		* BSON is
			* binary encoded Javascript Object Notation 
			* Transmits and stores data across web-based applications.
	* mongorestore
		* Import dump files from BSON
	* mongoexport
		* Export data to JSON or CSV
	* mongoimport
		* Import data from JSON or CSV.
	* An example of importing data into a Mongo database:
		* mongoimport --username="myuser" --authenticationDatabase="admin" --db=sample_data inventory.json
* Debugging Development
	* Good way is to check mongod.log
	* Disable the fork option as well.
		* In the configuration file
			* processManagement:
				* fork: true
	* Another good way is to check the Oplog file:
		* use local db.oplog.rs.find( { "o.msg": { $ne: "periodic noop" } }).sort( { $natural: -1}).limit(1).pretty()
		* db.oplog.rs.find( { "o.msg": { $ne: "periodic noop" } } ).sort( { $natural: -1 } ).limit(1).pretty()
	* Can also increase the log level.
		* db.getLogComponents()
	* Can change the above settings.
		* db.adminCommand({ setParameter: 1, logLevel: 2})
			* Have a higher log level, provides more verbose log output.
				* However, this can cause performance degredation.
* The Document Mode 
	* MongoDB natively works with JSON documents.
	* Can store JSON data without prior modification.
		* JSON has multiple key value pairs, where the keys define the data.
			* These must be strings.
		* The values are the ones that contain the data.
		* For example:
			* {
			* "course": "MongoDB Essentials",
			* "tags": ["databases", "document databases", "noSQL"],
			* "author": {
				"name": "Alice",
				"website": "mongodb.learn",
				"mastadon": "toot"
			}
		* Can use strings, values, booleans, arrays.
	* MongoDB use binary-encoded serialisation of JSON-like documents called BSON for storag .
	* BSON design lightweight and efficient.
	* BSON store binary data, such as images, timestamps and longs.
* Have one large database and inside that, multiple other databses.
	* Collections are groupings of documents.
		* Documents are the basic unit of data.
		* Each document contains one individual record.
		* Each document has a maximum size of 16MB
* How insert a document into a collection.
	* The collection "authors" is also created here.
	* db.authors.insertOne({"name": "Alice Smith"})
	* Each document in MongoDB must have  unique ObjectId value. If one is not given, MongoDB will automatically assign one.
* MongoDB Query Language (MQL)
	* Can also be referenced as MongoDB Query API
	* MQL allows perform CRUD operations.
	* JavaScript-based shell.
* insertMany command takes in an array of documents.
	* db.authors.insertMany([{ "name": "Bob"},{"name": "Kevin"},{"name": "Stuart"}])
* How to find a document within MongoDB:
	* db.authors.find({"name":"Alice"})
	* It doesn't matter if you put quotes around the field name or not.
	* For example:
		* db.authors.find({"name":"Alice"})
* How to update one document:
	* db.authors.updateOne({ name : "Alice"  }, { $set: { website: "www.soundsgood.com" } })
* How to update many documents at once.
	* How to update multiple documents, set the first field as empty.
	* The below example creates an empty array:
 		* db.authors.updateMany({  }, { $set: { books: [] } })
* How to delete a document:
	* db.authors.deleteOne({ name: "Alice" })
* How to delete multiple documents (literally deletes all of the documents within a collection):
	* db.authors.deleteMany({})
* Indexes and How They Work.
	* When you perform a query:
		* If you have no index, the database checks every document.
		* Called a collection scan.
			* No efficient.
	* Indexes are an organised way to look up data.
		* Store a subset of data with pointers.
			* These point to the location of full records.
	* If the query can be answered with an index, its called a covered query.
	* Provides more efficient queries and updates.
	* When should an Index be created?
		* When frequently query on same fields.
		* When frequently perform range-based queries on fields.
		* If have "Common Query Pattern"
			* Want an index on the pattern.
	* Indexes needs to be maintained:
		* Adds 10% write overhead.
		* Faster reads, but slower writes.
	* Must have enough RAM to fit the index.
	* Index Types
		* Single Field Indexes
			* Create an Index on only one field.
		* Partial Indexes
			* Add option to index to tell database to only match documents on a value that matches a certain condition.
		* Compound Indexes
			* Create Index on a combination of fields (useful if querying on multiple fields)
		* Multikey Indexes
			* Index on up to one array value.
				* It can't be more than 1 array value (it grows super quickly otherwise)
		* Text Indexes
			* Allow you to search within text fields.
		* Wildcard Indexes
			* Indexed on a field or set of fields.
				* But don't know the name of these fields, because the schema changes dynamically.
					* Should not be used otherwise.
		* Geospatial Indexes
			* (Geometric Indexes)
				* 2D Sphere indexes etc.
		* Hashed Indexes
			* Can reduce the index size.
				* If the original values are very large.
				* Not performant for ranged queries.
* How to create an index:
	* db.authors.createIndex({ name: 1  })
* Have to think about how the index will look up your data quickly.
* Durability in MongoDB
	* Guarantees acknowledged writes are permanently stored, even if the database or parts of it become temporarily unavailable.
	* Configuratble in MongoDB with a `writeConcern`
	* High Durability - Slower Writes
	* Low Durability - Faster Writes
	* An example of Durability:
db.authors.insertOne(
         { "name": "Alice" },
		 {
		          w: "majority",
				  j: "true",
				  wtimeout: 100
		 }
)
		* wtimeout, how long write operations should block for.
		* j option guarantees writes are all written to disk (takes longer however) or if they are okay to be written to the in-memory journal at the time the write is acknowledged.
		* If J is set to `true`, all writes have to be written to the disk and acknowledged.
		* If J is set to `false`, Operation reported as succeed, once the journals of enough mongods have the writes. Can cause issues if power is lost during the write process. 
		* If client issues `write` with the write concern as `majority`.
			* More than half of the data bearing replica set members in the deployment, must have the write, before the write acknowledgement is sent to the client.
			* One secondary must propagate the write, before the primary can acknowledge the write to the client.
			* Remaining nodes choose a new primary and continue working.
			* Higher write concern, makes data loss less likely.
	* If data integrity is important, set the `writeconcern` to `majority` and it helps with failovers.
* How Access Array Values
	* db.movies.findOne({"genres.0": "Musical"})
		* Lists all of the documents that have their Genre set as Musical.
* Find allows you to see only data that is majority committed .
	* How to set the readConcern:
		* db.authors.find({ <document>}).readConcern("majority")
		* readConcern can be the following:
			* local (default)
				* Returns most recent data on mongod conncected to.
					* No regard for majority connected data.
			* Available
				* Used for sharded clusters and similar to `local`.
			* Majority
			* Linearizable
				* Only majority of committed data only.
					* Waits for any current writes to complete, before reading and returning the data.
	* Can configure the readPreference
	* Allows application to route reads to secondaries.
		* primary (default)
			* All of the reads come from the Primary.
		* primaryPreferred
			* Allows reads to be writed to secondaries, the primary is still the preferred option.
		* secondary
			* Reads are routed directly to secondaries.
		* secondaryPreferred
			* Will only go to primary for certain circumstances.
		* nearest (lowest latency)
			* The node with the lowest latency to where you are querying from.
	* Risk reading stales data when reading from secondaries.
		* Fine for analytics.
		* Don't use it, if the goal is to increase your traffic capacity.
* Comparison Operators
	* $eq
		* =
	* $gt
		* >
	* $gte
		* greater than or equal
	* $lt
		*<           >
	* $lte
		*less than or equal to
	* $ne
		* Not equal to
	* Example commands:
	* db.inventory.findOne({ "variations.quantity": { $gte: 8 } })
		* Shows all of the documents that have a quantity of 8 or more.
	* db.inventory.findOne({ "price": { $lt: 1700 } })
		* Checks for a price that is lower than 1700.
	* $in
	* $nin 
	* Further Examples:
		* db.inventory.findOne({ "variations.variation": { $in: [ "Blue", "Red" ] } })
		* Gives us back 1 car, where the variation is "Red"
		* Searches for items that are only "Blue" or "Red"
		* db.inventory.findOne({ "variations.variation": { $nin: [ "Blue", "Red" ] } })
		* We only get cars that are NOT Blue or Red
* Logical Operators
	* $and (^)
		* Query for items that match multiple conditions.
		* db.inventory.findOne({ $and: [{"variations.quantity":{$ne: 0}},{"variations.quantity":{$exists: true}}]})
		* Checks for a document where the quantity is not equal to zero and that are documents exists.
	* $or (v)
		* db.inventory.findOne({ $or: [{"variations.variation": "Blue"}, {"variations.variation": "Green"}, {"variations.variation": "Teal"}]})
		* Finds a documen that is either Blue, Green or Teal
	* $nor (^)
		* db.inventory.findOne({ $nor: [{price: {$gt: 8000}}, {"variations.variation": "Blue"}]})
		* Checks for a car, where the price is not greater than 8000 and the variation is not blue.
	* $not (^)
		* db.inventory.findOne({ "price": {$not: {$gt: 2000}}})
		* Matches on the price field and a documents that is not greater than 2000.
* Sort, Skip, Limit
	* db.movies.find({}, {title: 1, director: 1, genres: 1}).sort({ title: 1})
	* Sorts movies by title.
	* Can sort results on multiple fields.
		* db.movies.find({}, {title: 1, director: 1, genres: 1}).sort({ director: 1, title: 1})
		* Checks for directors that start with the letter `A`.
	* How to use the Skip method:
		* This one skips the first 100 results:
			* db.movies.find({}, {title: 1, director: 1, genres: 1}).sort({ director: 1, title: 1}).skip(100)
				* Shows then the directors starting with the letter `B`.
	* Limit can "Limit" the results.
		* db.movies.find({}, {title: 1, director: 1, genres: 1}).sort({ director: 1, title: 1}).skip(100).limit(3)
		* Helps to limit the results to just 3 only.
	* When sort is a common query pattern, use an index.
	* If it is not a common query pattern, using sort with a limit is much faster regarding the algorithm used.
		* Mongo will always perform Sort, then Skip and then Limit in that order.
* updateOne and updateMany
	* If you run this and it matches multiple documents, only the first document matched will be updated.
	* an updateOne example:
		* db.authors.updateOne({name: "Alice Smith"}, { $set: {message: "Hello World!" }})
		* The above example adds the "message" field.
		* It was this before:
		*     _id: ObjectId("640924af841d3b1208bbf975"),
    name: 'Alice Smith',
    books: [],
		* Now it is this:
		*     _id: ObjectId("640924af841d3b1208bbf975"),
    name: 'Alice Smith',
    books: [],
    message: 'Hello World!'
	* an updateMany example:
		* You can match all by specifying an empty document in the first argument with {}
		* db.authors.updateMany({}, {$set: {message: "Hello" }})
		* Adds a message saying "Hello" to all fields.
	* Also unset operator:
		* db.authors.updateMany({}, {$unset: { message: "" }})
		* The above example removes the "message" field that we had before.
	* Commonly Used Update Operators:
		* { $set: {msg: "Hello world!"}}
		* { $unset: {msg: ""}}
		* { $inc: {quantity: -1, ordered: 1}}
			* Increases a value, either positively or negatively.
		* { $mul: {price: 0.9}}
			* Multiplies a field by a specified value.
		* {$max: {bid: 500}}
			* Updates the value to the specified value, ONLY if the value is not already at that level.
		* {$min: {lowest_available_price: 500}}
			} The opposite of max and only if the original value is not lower than the value specified.
* Arrays
	* Using Find:
		* db.movies.find({genres: "Comedy"})
		* Checks if Comedy has any value iniside the array.
	* Can specify an array of values:
		* db.movies.find({genres: [ "Comedy", "Drama", "Thriller"]})
		* Finds all movies that have Comedy, Drama and Thriller genres.
	* $all operator brings back documents that match everything within the array.
		* db.movies.find({genres: { $all: [ "Comedy", "Drama"]}})
	* $elemMatch --> Specifiy multiple conditions that have to be matched by one document in the array.
		* db.inventory.find({ variations: { $elemMatch: { variation: "Blue", quantity: {$gte: 8} }}})
* How to update arrays as well.
	* $push can add more fields.
	* An example below of adding a field called "test" to the available genres.
	* db.movies.updateOne({_id: ObjectId("63fd50eaf2d7bf128c7ca0d5")}, {$push:{genres: "Test"}})
	* How to find that document you updated again:
		* db.movies.findOne({_id: ObjectId("63fd50eaf2d7bf128c7ca0d5")})
	* $addToSet
		* Only adds the elements we specifiy, if it is NOT already present in the array.
		* An example of $addToSet below:
			* db.movies.updateOne({_id: ObjectId("63fd50eaf2d7bf128c7ca0d5")}, {$addToSet:{genres: "Test"}})
		* How to REMOVE things from an array.
			*$pop operator.
		* This will remove the LAST item in the array genres array, for example if there was "test" and "green", it would remove "green", but "test" would still be there.
			* db.movies.updateOne({_id: ObjectId("63fd50eaf2d7bf128c7ca0d5")}, {$pop: {genres: 1}})
		* To remove the FIRST element in the array:
			* Use -1 instead of 1
			* db.movies.updateOne({_id: ObjectId("63fd50eaf2d7bf128c7ca0d5")}, {$pop: {genres: -1}})
* Transactions
	* An operation on a single document is atomic.
	* If there are two people and one writes and one reads, the document will either be read to first or written to first.
	* Multi-document Transactions
		* When someone makes multiple changes to a document.
		* Guarantee atomicity of reads and writes to multiple documents.
		* Reads return all documents in the state they were when the read began.
		* Either all writes occur or none occur.
	* Transactions can be used across Operations, Documents, Collections and Databases.
	* How to Create a Session Objects:
		* session = db.getMongo().startSession({ readPreference: { mode: "primary"} })
		* To start the sesssion:
			* session.startTransaction()
	* How to use Transactions.
	* session.getDatabase("blog").authors.updateMany({},{$set: {message: "Transaction occured"}})
		* How to update multiple documents.
		* To End a Session:
			* session.endSession()
	* Overuse of transactions, leads to performance degredation.
		* If you need transactions, check the data model.
* $expr
	* Can compare different document values.
	* db.movies.find({},{title:1, ratings:1})
		* Good way to find go throug all matching documents.
		* The $ is required in front of it, for the string literal.
		* An example of $expr:
			* db.movies.find({$expr:{$gt: [{$multiply: ["$ratings.mndb", 10]},"$ratings.soft_avocadoes"]}})
				* This multiplies the mndb rating by 10 (to make the rating out of 100, which is the same rating that the soft_avocadoes scale uses) and can then be compared.
		* $expr has a lot of operators that can be used with it.
	* Any common operations used with progrsamming, can be done with programming as well.
		* Look up Aggregation Pipeline Operators on the MongoDB Documentation.
* Aggregation Pipeline
	* db.collection.aggregate( [] )
		* This is how you start it out. To use operators.
	* $group
		* grouping patterns are useful for grouping data.
		* Specify with $ value, because we want to get the value of the field.
		* An example would be:
		* db.inventory.aggregate([{ $group: { _id: "$source"}}])
		* Then it produces an output such as:
		[
  { _id: 'Jetpulse' },   { _id: 'Brightdog' },
  { _id: 'Mudo' },       { _id: 'Browsedrive' },
  { _id: 'Skivee' },     { _id: 'Voolith' },
  { _id: 'Skibox' },     { _id: 'Babbleblab' },
  { _id: 'Realbridge' }, { _id: 'Avaveo' },
  { _id: 'Yacero' },     { _id: 'Thoughtbridge' },
  { _id: 'Yadel' },      { _id: 'Gigaclub' },
  { _id: 'Meedoo' },     { _id: 'Yodo' },
  { _id: 'Ozu' },        { _id: 'Gabtype' },
  { _id: 'Camido' },     { _id: 'Skiptube' }
]
		* Using $sum adds one. An example is:
			* db.inventory.aggregate([{ $group: { _id: "$source", count: {$sum: 1}}}])
		* Which gives an output such as:
		[
  { _id: 'Shufflester', count: 5 },
  { _id: 'Pixoboo', count: 3 },
  { _id: 'Skinder', count: 2 },
  { _id: 'Omba', count: 3 },
  { _id: 'Browsezoom', count: 2 },
  { _id: 'Skiptube', count: 1 },
  { _id: 'Zava', count: 2 },
  { _id: 'Gabtype', count: 2 },
  { _id: 'Camido', count: 2 },
  { _id: 'Meedoo', count: 5 },
  { _id: 'Yodo', count: 2 },
  { _id: 'Ozu', count: 1 },
  { _id: 'Yadel', count: 3 },
  { _id: 'Gigaclub', count: 4 },
  { _id: 'Yacero', count: 1 },
  { _id: 'Thoughtbridge', count: 2 },
  { _id: 'Realbridge', count: 2 },
  { _id: 'Avaveo', count: 3 },
  { _id: 'Babbleblab', count: 4 },
  { _id: 'Browsedrive', count: 1 }
]
		* This one adds an array of car names in the "items" field:
		* db.inventory.aggregate([{ $group: { _id: "$source", count: {$sum: 1}, items: { $push: "$name"} }}])
		  {
    _id: 'Babbleblab',
    count: 4,
    items: [ 'Land Rover', 'Hummer', 'Toyota', 'Oldsmobile' ]
  },
  { _id: 'Jetpulse', count: 1, items: [ 'Toyota' ] },
  { _id: 'Browsedrive', count: 1, items: [ 'Hyundai' ] }
		* You can see the average price as well:
		* db.inventory.aggregate([{ $group: { _id: "$source", count: {$sum: 1}, items: { $push: "$name"}, avg_price: {$avg: "$price"} }}])
* $bucket
	* Instead of grouping by one value for all documents, you define bucket ranges for a value.
		* If the values fall into that range, they will be placed into that particular bucket.
	* This example will place different documents into separate buckets and any other documents that don't fit into that, will go into the `Other` category.
	* Example output:
	  { _id: 1980, count: 85 },
  { _id: 1990, count: 340 },
  { _id: 2000, count: 431 },
  { _id: 2010, count: 127 },
  { _id: 'Other', count: 17 }
	* How to add more context than just count:
	* db.inventory.aggregate([{$bucket: {groupBy: "$year", boundaries: [1980,1990, 2000, 2010, 2020], default: "Other", output: { count: {$sum: 1}, cars: { $push: {name: "$name", model: "$model"}}}}}])
	* An example output:
	    _id: 'Other',
    count: 17,
    cars: [
      { name: 'Chevrolet', model: 'Camaro' },
      { name: 'Volkswagen', model: 'Beetle' },
      { name: 'Pontiac', model: 'Grand Prix' },
      { name: 'Pontiac', model: 'Grand Prix' },
      { name: 'Pontiac', model: 'Grand Prix' },
      { name: 'Plymouth', model: 'Volare' },
      { name: 'Porsche', model: '914' },
      { name: 'Chevrolet', model: 'Camaro' },
      { name: 'Pontiac', model: 'GTO' },
      { name: 'Chevrolet', model: 'Monte Carlo' },
      { name: 'Chevrolet', model: 'Vega' },
      { name: 'Ford', model: 'Mustang' },
      { name: 'Ford', model: 'Thunderbird' },
      { name: 'Dodge', model: 'Charger' },
      { name: 'Studebaker', model: 'Avanti' },
      { name: 'Austin', model: 'Mini Cooper S' },
      { name: 'Pontiac', model: 'GTO' }
	* $bucketAuto
		* Automatically define the boundary and distributes fairly between all groups.
	* An example of $bucketAuto
		* db.inventory.aggregate([{$bucketAuto: {groupBy: "$year", buckets: 5 }}])
* $unwind
	* Create one output document for each array element.
	* db.inventory.aggregate([{$unwind: "$variations"}])
		* Shows individual documents for each car variation.
	* db.inventory.aggregate([{$unwind: "$variations"}, {$match: {"variations.variation": "Purple"}}])
		* Matches only on the colour purple and only shows purple cars.
	* To make the query more efficient, you can add the following:
		* db.inventory.aggregate([{$match: {"variations.variation": "Purple"}},{$unwind: "$variations"}, {$match: {"variations.variation": "Purple"}}])
* $out
	* Store output of aggregation pipeline into new collection.
	* An example:
	* db.inventory.aggregate([{$match: {"variations.variation": "Purple"}},{$unwind: "$variations"}, {$match: {"variations.variation": "Purple"}}, {$out: { db: "sample_data", coll: "purple" }}])
	* Creates a collection, only containing purple cars.
	* db.purple.find({})
$merge
	* Similar to $out.
		* Also allows to merge results into an existing collection.
	* A good example of this:
		* db.inventory.aggregate([{$match: {"variations.variation": "Purple"}},{$unwind: "$variations"}, {$match: {"variations.variation": "Purple"}}, {$merge: { into: "purple", on: "_id", whenMatched: "keepExisting", whenNotMatched: "insert" }}])
* $function
	* Allows writing of Javascript functions, that operate on the field values of the documents.
	* An example:
		* function custom_agg_expression(actors) {return actors.sort();}
	* db.movies.aggregate([{$project: {title: 1,actors:{$function: {body: "function(actors) {return actors.sort(); }", args: ["$actors"],lang: "js"}}}}])
		* Shows the titles and actors in alphabetical order.
* lookup
	* For example, we have Orders and Inventory
		* Can merge information from both documents, for example matching the car ID fields from both Orders and Inventory.
	* An example:
		db.orders.aggregate([{$lookup:{from: "inventory", localField: "car_id", foreignField: "_id", as: "car_id"}}])
	* Pulls in information regarding the car ID:
	* Here is the output:
		    _id: ObjectId("622fc4ebf464966bf901547c"),
    name_id: 'Pamela Franzelini',
    price: 17242.17,
    credit_card: '3562980000615614',
    credit_card_type: 'jcb',
    car_id: [
      {
        _id: '120983921-0',
        name: 'Nissan',
        model: 'GT-R',
        year: 2010,
        price: 17642.36,
        source: 'Jabbercube',
        sale_frequency: 'Daily',
        variations: [ { variation: 'Green', quantity: 12 } ]
      }
	* Must create an index on the foreignField.
		* The performance will be degredated otherwise.
	* Common query patterns rarely require joins.
		* If use a lot of lookups, not structuring data well for MongoDB.
		* Data you query together, should be in the same documents.
* Performance
	* Aggregation pipelines generally require more RAM and CPU than CRUD operations.
		* Large data.
		* Run frequently.
		* Operation needs to be fast.
	* Example query:
		* db.movies.explain("executionStats").aggregate([{$project: {release_year: {$year: "$release_year"},title: 1}},{$lookup: {from "inventory", localfField: "release_year", foreignField: "year", as: "year"}}])
	* When query plan goes up to certain threshold of results, that query plan becomes the winner.
	* Collection Scan --> Checks for all results in certain collection.
		* 1000 movies and 1000 cars, the database has to check everything.
	* Total Keys Examined: If 0, then no index was used.
	* Collection Scans
		* Can see slow queries in MongoDB logs and why they were slow.
		* Because a query does not show up in the MongoD logs, doesn't necessarily mean that it is fast.
			* If they are slower than 100ms, they are not logged in the MongoD logs.
	* Use the Native Profiler
		* db.setProfilingLevel(1, {slowms: 20})
			* Finds operators that are slower than a certain amount of MS.
			* This profile with low MS values can slow down the deployment.
	* Common operations:
		* $sort + $limit
			* Makes it possible to perform sort operations faster.
		* $project as the final stage.
		* Not better to project early in the pipeline.
		* Optimiser will do that for you.
		* Hinting
			* Can tell an aggregation pipeline to use a specific index, if it is using a less optimal one by default.
			* db.collection.aggregate(pipeline, {hint: "index_name"})
		* Analytics nodes
			* If running a lot of aggregations and impacting performance.
				* Can run multiple analytics secondary nodes as well, to stop performance.
			* If notice aggregation pipelines slowing down MongoDB.
				* Require to kill the operation.
				* db.currentOp(true)
				   db.adminCommand({"killOp":1, "op": OP_NUMBER})
					* Re
	
		* Can use a specific Index if using an op
* Relational vs. Document Models
	* Relational DBs are structured in tables.
		* When querying data, you join multiple tables together to gather the information.
	* Storing JSON documents.
		* Supported by both.
	* Relational databases store JSON in blobs.
		* MongoDB just stores JSON files.
	* Relational DBs - good performance, but that's about it.
	* Document - optimal performance.
		* Store all JSON documents as they are.
		* BSON makes operations for documents much more efficient.
	* Storing tables
		* Data from a person or an other is done via `joins`.
			* Can perform `joins` using the `$lookup`:
		* Example:
			* db.orders.aggregate([{
					$lookup: {
						from: "inventory",
						localField: "car_id",
						foreignField: "_id",
						as: "car_id"
					}
				}])
		* Relational models are optimised for working with tables and jooins.
		* MongoDB is not optimised for working with tables and joins primarily.
	* Storing data in the data models best for each database.
* Which one is better for querying?
	* Can query MongoDB with SQL.
	* Consider:
		* Performance.
		* Ease of development
		* Learning time
		* Scale
			* Joins only perform quickly, if tables are located close to each other.
			* More performant to scale horizontally with sharding.
* Data modelling
	* Data commonly queried together should live close together.
	* 16 MB document limit.
	* Aggregation pipeline processing limits.
		* Performance is better with small documents.
	* One-to-one relationship;
		* Person + DOB for example.
		* The documents gets too big.
		* Rarely use information.
	* One-to-many relationship.
		* One to few - store both in one collection using nesting or arrays.
			* Authors and Books for example
		* One to many - store them separately with links.
	* Many-tomany relationship
		* Don't embed the informtion.
			* Store IDs in either one or both collections.
	* Keep arrays small --> Less than 100 elements.
	* Documents should not be large or flat.
* Flexible Schema
	* Schema defines structure and contents of data in colleciton.
		* Documents contain fields marked as "required".
		* Documents field values conform to specified data types.
	* Example:
		* validator: {$jsonSchema: {
	   		bsonType: "object",
				required: [ "name", "message"],
					properties: {
						name: { bsonType: "string",
										description: "must be a string and is required"},
						message: { bsonType: "string",
										description: "must be a string and is required"}
	}}}
		* Schema validation is not required:
			* Easy to iterate.
* Documents should have a common structure.
	* To force a schema:
		* Here is an example:
			* db.runCommand({ collMod: "movies", validator: { $jsonSchema: { bsonType: "object", required: ["title", "director"], properties: { title: { bsonType: "string" }, director: {bsonType: "string" }}}}, validationLevel: "moderate" })
	* Then if you try to insert a new document, the schema will check the document and either accept or reject it.
* MongoDB Drivers
	* Can interface with Mongo via Python and so on.
		