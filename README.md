# RAG Retail Inventory Agent #

Hi!

This is a prototype Langchain agent webapp particularly useful for situations when customers inquire about the location of a specific product or its stock status (especially when the vending shelf appears empty).

A great use case for this would be to connect the LLM-agent to a SAP inventory management system SQL database and display the app on a work phone.
A prime application of this tool would be its integration with a SAP inventory management system's SQL database, allowing the app to be displayed on a work phone for easy access. To avoid the need for creating a specific SQL database for this demonstration—and since SQL agents operate in a manner very similar to CSV agents—we've opted to design an imaginary supermarket inventory using a CSV file for this project. (**Important: the file is UTF-8 encoded and uses commas for separation.**)

The following libraries are needed for the project:

- os (for setting the OpenAI API-key as an environment variable)
- langchain
- streamlit (for creating prototype webapps)

As always, the code is thoroughly commented.

Have fun!

<img width="683" alt="webapp_screenshot" src="https://github.com/march038/RAG-Retail-Inventory-Agent/assets/140447879/90e11fd0-fa52-4e3c-8b71-e8cf56d9ff57">
