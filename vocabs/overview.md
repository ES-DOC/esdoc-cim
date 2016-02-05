### Introduction  
There is a strong requirement to deliver a comprehensive, cross-project, controlled vocabulary (CV) service.  Such a service would take responsibility for hosting controlled vocabularies and providing really simple tools to streamline CV interaction.  At it's heart such a service would facilitate constraining metadata so as to improve quality and to simplify downstream software artefacts such as search engines and user interfaces.  

### Definition  
A CV is simply defined as a **managed collection of terms**.  A CV service manages **multiple themed collections** and provides programmatic access to those collections.

### Types  
Most CV's are simple sets of terms, i.e. flat lists.  However some CV's are hierarchical sets of terms.  Some terms are associated with terms from other collections, i.e. collections can be coupled.

### Scoping  
CV's may be scoped at the global level (e.g. set of institutes) or at the project level (e.g. set of models).  

### Client Tools
A CV service should provide client tools in an array of programming languages.  Each tool will implement [a standard programming interface](https://github.com/ES-DOC/esdoc-cv/wiki/programming-interface).  It is essential that the tools are extremely simple to install and use.

### Governance  
External committees are responsible for mandating and managing CV's.  Committees will update CV's on a frequent basis.  There needs to be a structured workflow in place to reflect and support the decisions of the committees.    

### Versioning  
A CV update consists of a term being either added, updated or deprecated.  A full version history of such updates needs to be maintained.      

### Meta-information
CV's need to be associated with meta-information in order to support governance, identification, versioning, human readability, scoping ...etc.  Whilst at both the collection and term level a core set of meta-information is mandated, an extensible set of meta-information should also be supported.  

### Repository  
A CV repository will need to be created using some form of version control system such as git.  

### Encodings
CV's will need to be encoded in several encodings.  JSON should be considered as the primary encoding due to it's simplicity of use in a wide array of programming languages.  Convertors will convert the primary JSON encoding to other encodings such as XML, SKOS, RDF ..etc.  [Sample encodings can be found here](https://github.com/ES-DOC/esdoc-cv/wiki/sample-vocabs).

### API
A remote API could be developed.  This would provide implement the standard programming interfaces as a set of web-service endpoints.

### Target Vocabs  
* **[esgf search facets](https://github.com/ES-DOC/esdoc-cv/wiki/vocab:-esgf-search-facets)**  
* **[cim v1](https://github.com/ES-DOC/esdoc-cv/wiki/vocab:-cim-v1)**  
* **[cf names](https://github.com/ES-DOC/esdoc-cv/wiki/vocab:-cf-names)**  

### Work plan
[Detailed work plan is documented here](https://github.com/ES-DOC/esdoc-cv/wiki/work-plan).