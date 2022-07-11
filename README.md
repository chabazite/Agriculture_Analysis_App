# Agriculture Analysis Dashboard
==============================

## Business Case
<a name="Business_Case"></a>

As the population on earth continues to grow, so too does the demand placed on the agricultural industry. 

Our society has always grown at the hands of improvements to this industry. There have been three major agricultural revolutions throughout human history. With each, comes a drastic increase in humanity ability to sustain larger populations. 

 **Neolithic Revolution**
The first revolution saw humans transition from a hunter-gatherer species, to one of organized communities and agriculture. While many improvements such as irrigation came at this early stage, the domestication and selective breeding of cereal grasses set the stage for agriculture as we know it today. 

**British Agricultural Revolution**
While this time period is dominated by the onset of the industrial revolution, the second agricultural revolution has been cited as the cause for this drastic shift in society. Again main advancement through the british agricultural and industrial revolution propelled humanity into another great population boon. Many historians credit one of the most important advancement to be the Norfolk four-course rotation. This new stype of crop rotation, increased soil fertility through the use of nitrogen-fixing clover, as well as providing winter turnips, which utilized deeper soil nutrients due to its root structure. It’s possible this increase in productivity for both crops and workers is what allowed for the industrial revolution to boom.

**Green Revolution**
Starting in the 50s and 60s, the third great agricultural revolution began. This revolution had widespread impact on a reduction in land use, poverty, worldwide hunger, and even infant mortality. This was due to advancements across the board in agricultural chemical use including pesticides and fertilizers, high yield seeds, and the introduction to modern machineries. 

While these revolutions have paved the way for our population growth, none of them were without their pain points and each of them have successively led to an reduction in finite resources of our earth. 

How has the Green Revolution changed humanity and the way we steward our limited and ultimate resource of land?

1. What kind of change has the world seen in population ?
2. How has land development changed?
3. How have living conditions been impacted?
4. How has Agriculture demand and economics changed? 
5. How have major world issues changed?


Check out my medium post <a href="#">here</a>

## Table of Contents
<details open>
  <summary>Show/Hide</summary>
  <br>
 
1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Structure ](#Structure)
4. [ Evaluation ](#Evaluation)
5. [ Future Improvements ](#Future_Improvements)

</details>


## Project Organization

<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
 <br>


    ├── LICENSE
    ├── .gitignore
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── agenv                <- Virtual Environment for the project
    │
    ├── dashboard_app      <- Folder that contains all deployment needs
    │   ├── images         <- directory of images for the app
    │   ├── templates      <- html webpages
    │       ├── index.html    <- 
    │       └──               <- 
    │   ├── __init__.py    <- 
    │   ├── routes.py      <- 
    │   └──                <- 
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── setup.py           <- makes project pip installable (pip install -e .) so src can be imported 

--------
  </details>   

## Technologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>

      
    ├──AWS Lightsail
    ├──Docker
    ├──Python
        ├──Numpy
        ├──Pandas
        ├──Flask
        ├──Requests
        ├──Matplotlib
        ├──Seaborn
        └──
 
 ------------
 </details>

## Structure of Notebooks:
<details>
<a name="Structure"></a>
<summary>Show/Hide</summary>
<br>

 1. API Practice
      * 1.0 Learning how to utilize the Worldbank API
 2. API Data Wrangling
      * 2.0 Importing and cleaning indicators from worldbank
      * 2.1 Population APIs
      * 2.2 Land Development APIs
      * 2.3 Living Conditions APIs
      * 2.4 Agricultural Practices APIs
      * 2.5 World Issues APIs
 3. Exploratory Data Analysis
      * 3.0 Importing
      * 3.1 Question 1: Population
      * 3.2 Question 2: Land Development
      * 3.3 Question 3: Living Conditions
      * 3.4 Question 4: Agricultural Practices
      * 3.5 Question 5: World Issues
     

 </details>

## Evaluation:
<a name="Evaluation"></a>
<details>
<summary>Show/Hide</summary>
<br>
This project was indeed successful in creating a minimum viable product (MVP) that can generate the basic stats of a monster given a few simple inputs! Check out the medium post <a href="https://medium.com/@Andrew-Ingalls/using-tensorflow-to-build-a-balanced-dnd-monster-generator-c942f4456626" target="_blank">here</a> as I go into further detail regarding the process and my answers for the questions in the <a href="#Business_Case">business case</a>.

I was able to uncover high variance in some of the categorical variables such as monster type, size, alignment, and environment, which led to a more robust predictive model. Sadely, the environment was the least impactful of these variables. I was also able to find strong correlations between the output variables like stats, saving throws, damage, hit points, and armor class. This was one of the major factors that led me to switch over to a Keras model in TensorFlow. The outputs are able to help inform each other in a neural network, creating a more robust model over the simplistic regression models. In fact, the accuracy went from around 60% to over 85% by switching over to the TensorFlow neural network.

Finally, I’m excited to say I was able to dockerize and deploy a basic app using AWS Lightsail and Plotly’s Dash, which is housed on the Flask framework. This allowed me to send the model to other DMs for critiques and further testing! Here is a link to the <a href="https://dnd-monsters.b5171qf35pc3s.us-west-2.cs.amazonlightsail.com/" target="_blank">app: DnD Monster Generator</a>. 

</details>
  
## Future Improvements
 <a name="Future_Improvements"></a>
 <details>
<summary>Show/Hide</summary>
<br>
While I was able to create a deployed app for our model, it’s far from complete. Moving forward there will need to be a lot more testing, refining, and features built out to make this a stable and usable app for Dungeon Masters. The first step will be, using this app, discussing with other Dungeon Masters how useful this tool is to them and what kind of improvements they would like to see. 
      
From there, I can already see the following will need to be addressed:
 1. Fine tuning model further. I would like the stats to reflect the monster type shape more consistently
 2. Finding a way to incorporate spells and spell damage into the inputs and/or outputs
 3. Allow for more variety in inputs (e.g., spellcaster, player character magic items, flying traits)
 4. Increase the number of traits available in output
 5. Upgrade the UI of the model 

</details>

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
<p>README outline tailored from [awesomeahi95][]<p>