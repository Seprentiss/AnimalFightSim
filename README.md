# AnimalFightSim
## What is the Animal Fight Simulator
The Animal Fight Simulator came about after having a discussion with my father about whaht animal would win in a fight.
<br> I used to have these debates all the time as a kid with my friends and now that I know a bit about programming I set out to answer the question
of which animals really would win in a head to head matchup.

## How are winners decided

The method by which the winner is decided is by using a Monte Carlo simulation to run 10,000 fights and calulacte the percentage of total victories for each combatant.

For those who don't know what a Monte Carlo Simulation is, it's a method to model the probability of different outcomes in a process where the outcome cannot be easily predicted due to the intervention of random variables.

The random variables in this case are the stats of the Animals and the location of the fight. <br>They can range from the bite force of the animal to how often does it climb trees in certain enviornments. <br> How did I create these stats? I will explain that in a further section.

After the variables are inputed and calculted the simulation spits out a winner and what percentage of fights it would win.

## Stats and How were they were created
For this project to be even remotely accurate I had to get the stats of each animal correct. First I had to decide which stats I wanted to use and how I would incorporate them into the simualtion. For this project I created 17 different stats.

### Aggression<br>
Aggression is a measure of how likely an animal is to attack first. For example a gorilla is very unlikely to initiate a fight and often flee if their threat tactics do not work. An animals agression is rated on a scale form 1 to 100. I calculated this number via researching each animals aggressive tendencies and how likely they are to attack humans in the wild. The way this stat is implemented in the simulation is that the more agressive an animal is the more likey it is to go first in the fight and vice versa. 
<br>
### Agility<br>
Agillity is a measure of an animals ability to move quickly and easily. Its calculated using a formula that is based around the animals speed and size. Its use in the simulation is to help calculate an animals evasiveness score.
<br>
### Attack Per Turn<br>
Attck Per Turn is a very important stat since the simulation is turn based this stat dictates how many attacks an animal gets per turn. Its caluated using the animals Speed, Agillity, Stamina, and Size stats.
<br>
### Bite Force<br>
Bite Force is simply how hard can the animal bite. Since a lot of animals have a bite attack its used in calculating the damge done by the bite attack. 
<br>
### Bleed<br>
Bleed is a stat used to calcualte the damage inflicted on an animal if its bleeding after an attack. Its calculated using the animals Size, Duarabillity, and Health.
<br>
### Durability<br>
Durabilliy attempts to make the durabllity of an animal numeric. To do this i looked at each animlas natural defenses like fur, hide, and layers of fat. I also looked at how much damge/ effort it takes other animals to take it out(if i could find video or information). Duarbillity is scored on a sclae of 1 to 100 and contributes to a bunch of different stats
<br>
### Evasiveness<br>
Evasiveness is a stat used to detremine how likely an animal is to dodge an attack. When ever an animal uses an attack its opponent has a chance to dodge the attcack. The probabillity it dodges the attack is based off of its evasiveness.
<br>
### Health<br>
Health determines how many hitpoints an animal has. It's calculated using an animlas Size and Durabillity.
<br>
### Height<br>
An animals height. Used in calculating the Size stat
<br>
### Intelligence<br>
Intelligence shows how intelligent an animal is on a scle of one to 100. Each animals Intelligence was scored after doing research on each animal. I looked at how atricles and papers that compared animal intelligence to humans and scored each animal based off of that.
<br>
### Size<br>
Size is a measure of how 'Big' an animal is. Its hard to compare animals Heights and weight. So i created a formula to combine the two and give each animal a size score making easier to compare sizes.
<br>
### Speed<br>
How fast an animal is. Speed is used in multiple calculations for other stats. Speed is measured in kilometers per hour.
<br>
### Stamina<br>
Stamina attempts to measure how long an animal can last in a figh before getting tired. Big cats are nortoious for having low stamina, where as wolves have been known to run for miles before getting tired. Stamina tries to encapsulate this and incorporate it into the simulation. Stamina is rating on a scale of 1 to 10 and  is used in calculating Attacks Per Turn.
<br>
### Strength<br>
Strengthh attempts to measure how strong an animal is. To calculate it I looked at how much weight an animal has been recored to have pulled, pushed, or lifted. In cases where that has never been recorded i had to use expert hypotheses or make educated guesses based off of the strength of known animals. Strength is measured in Kg.
<br>
### Weight<br>
An animals weight. Used in calculating the Size stat
<br>

Creating these stats took hours of research. I looked at every resource I could find be it video, well sourced web articles, or expert research  I had to look into many different characteristics of each animal. I also has to create tendencies for each animal. Tendencies like how often do they climb trees, do they camoflaugue themselves in certain enviornments etc.

Throughout testing some of the stats had to be adjusted slightly for balancing purposes.

## Overall experience/ What I learned
This project taught me a lot. I was able to sharpen my coding skills as well as fully complete a project from start to end without a prior template being provided.
I learned how to create metrics and how to balance them to achieve results and learned how to create a Montecarlo Simulation. I thouroughly enjoyed this project and had a blast working on it. I'll be continuing to update it with further features like more animals and terrains.
