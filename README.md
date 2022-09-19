# Player Contribution Prediction

In this Project we are using a 2021-2022 season player statistics dataset to predict weather a new player is expected to have a goal contribution (goal or assist) greater than 20. (having over 20 contributions in a season is usually the indicator of an impactful player). 

### Preparing the Environment

To set up the environment we have our requirements.txt file which holds all the packages we need to install for this project as well as our makefile which which which do the install, format, lint and test. In addition we have our devcontainer and dockerfile which will house the environment for this project. Lastly we create the .yml file that will automate our makefile procedures upon each push.

### Process

Our dblib subfolder we have several scripts that interact with one another. get_sql_table connects to the databricks cluster and pulls in our data. preprocess then preprocesses the data so it can be ingestible by the model. knn_predict holds the knn object, and lastly, predict_impact puts it all together. 

### Workflow diagram
![Diagram](/Users/danyjabban/Desktop/tree_split.png)

### Command Line Tool

We can then use our command line function and choose a player to predict his goal contribution using the commane:
python ./player_contribution_predictor.py cli-predict --player "player_name"



