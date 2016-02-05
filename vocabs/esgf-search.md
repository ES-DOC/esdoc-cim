`Are these facets CMIP5 specific ?`

* **Project**
	- should be revisited, as the project value controls which vocabulary to use. There is some need to limit the values it can assume, but on the other hand we do not want to make it hard for users to register and create new projects, for example in CoG. Maybe we need to distinguish between projects that publish data, and projects that are created to support a scientific goal of some kind

* **Model**: should be regulated by CV

* **Experiment**: should follow CV

* **Experiment Family**: CV

* **Ensemble**: we should not try to completely control this facet as there are too many values, but rather upgrade the software to enforce a regular expression"rXiYpZ". There was general agreement that Ensemble is still useful as a facet

* **Instutute**: CV

* **Product**: CV. At a later time, this facet could be better defined or evolved.

* **Realm**: CV

* **Cmor_table**: to some extent, this facet overlaps with Realm. It was decided to keep it as a facet for now, but leave any decision of a CV for later on

* **Time Frequency**: CV

* **Variable**: after some discussion, it was decided that a project like CMIP5 should be able to enforce a CV to allow consistent naming and searching across files. Other projects, like ana4MIPs, should be able to decide to use the same CV as CMIP5, and perhaps expand it with additional terms, or use no CV at all. 
The ESGF publishing infrastructure already supports the use of different CVs for different projects.

* **Variable Long Name**: it was decided to NOT control this facet as a CV

* **CF Standard Name**: the possible values are already controlled by the CF specification. ESGF should be able to parse the official list and use it to enforce correct values.