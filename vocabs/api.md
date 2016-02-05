A CV service should provide client tools in an array of programming languages. Each tool will implement a standard programming interface.  Whilst this interface is expected to be implemented in python, java and javascript, the various implementations are free to only implement a subset of the full interface according.   

* **validate**  
Validates whether a collection contains a named term  
in: collectionID, term  
out: boolean  

* **validateRelation**  
Validates whether a hierarchical collection supports a relationship between two terms  
in: collectionID, termA, termB  
out: boolean 
 
* **get**  
Retrieves a collection  
in: collectionID  
out: collection  

* **getSet**  
Retrieves a set of collections   
in: collectionIDSet  
out: collectionSet    

* **getAll**  
Retrieves all collections   
out: collectionSet    

* **getTree**  
Retrieves a hierarchical collection representation   
in: collectionID  
out: collection  

* **encode**  
Encode a collection   
in: collection    
in: encoding  
out: unicode encoding representation   

* **decode**  
Decodes a collection representation 
in: repr  (a unicode representation of a collection)    
in: encoding  (json | xml | skos)
out: collection   

* **read**  
Reads a collection from a local disk  
in: filename  
out: collection   

* **write**  
Writes a collection to a local disk  
in: collection    
in: filename
