INTRODUCTION
############
GIS based technologies have been sufficiently proved in some sustainable development projects carried out in Africa related to international cooperation as well as in local development where the cross-sectorial work is critical.

Our team used the geolocation data from call detail records extracted from Orange's customer base in order to know in which areas the customers have been moving around, to help us discover the morning and evening rush hours: the time when users were commuting between their place of residence and their place of work.

MODEL
#####
In our model, the temporal component is useful for providing a tool to move backward and forward in order to get a more detailed understanding of the dynamics, not only moving across the timeline, but by creating temporal windows to group events. The geographical component provides a more high-level understanding related to the human mobility across the space at different levels, and connecting it to some other spatial features.

METHOD
######
Using the antenna's position and the traffic intensity, a kernel function has been used to calculate a weight density in a neighbourhood around those points.

Our kernel function is based on the quadratic kernel function. Conceptually, a smoothly curved surface is fitted over each point. The surface value is higher at the location of the point and diminishes with increasing distance from the point, reaching zero at the 'search radius' distance from the point.

The volume under the surface equals the 'population field' value for the point. The density at each output cell is calculated by adding the values of all the kernel surfaces where they overlay the center of the cell.

HYPOTHESIS
##########
Our hypothesis is that we can automatically identify the different stages of the commuting process from the data provided, creating a commuting profile of the studied area.

The main idea behind this reasoning is that people usually move early in the morning from their home to the place of work (first peak), stay there for some time (plateau), and finally, travel back to their home (second peak), closing the cycle.

RESULTS
#######
 + A clear distinction between dynamic and static groups and their evolution through time for the different regions conforming the Ivory Coast was found.

 + We were able to identify the three different stages of the commuting process from the data provided, verifying our hypothesis.

CONCLUSIONS
###########
 + Knowing people dynamics and, specially, commuting patterns, constitutes a great tool for improving infrastructure, logistics, and communications in general.

 + A simply anonymized dataset does not contain name, home address, phone number or other obvious identifier. Yet, if individual's patterns are unique enough, additional information can be used to link the data back to an individual.

 + Mobile devices are a great tool for real time sensing. Being almost everywhere, they can be of great help in acquiring data for generating more accurate predictive models.

FUTURE WORK
###########
 + Apply our model to automatically identify the commuting profile for different places.

 + Create geographical and time-based prediction models to better manage logistics and infrastructures.

 + Reinforce prediction models with sentiment analysis extracted knowledge.

 + Use the commuting profile of a region for outliers detection, anticipating possible critical events or unusual activity.

ACKNOWLEDGEMENTS
################
To Prof. Antonio Hernando Esteban (Automatic & Systems Engineering dept. at EUI-UPM) to review the mathematical formalism proposed in this paper.

Also Carmen Vidal, Operations Manager at Paradigma Tecnologico to support this project and the people at Paradigma Labs.
