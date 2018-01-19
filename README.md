# Assignment1 - Practice Designing Models


> * Participant name: Rachel Straney
> * Project Title: Dogs Helping Pets - A Community Network to Aid in Finding Lost Pets

## General Introduction

Having a lost pet can be an upsetting and stressful experience. Common resources and activities that people rely on to locate their pets include physically searching in the area, posting signs in the neighborhood and visiting local animal shelters. Some owners of lost pets will use social media platforms like Nextdoor or Facebook to communicate with their neighbors regarding their lost pet – a sort of virtual ‘Lost Pet’ sign. Sometimes pet owners go to great lengths to find their lost pet, including hiring professionally trained tracking and trailing dogs to locate the lost animal. The purpose of this post is to propose a technology driven solution to reunite lost pets with their owners and driving Orlando in the direction of becoming a smart city.

![Image of Smart City](images/Dog_and_Cat.jpg)

#### Purpose of this Network
The inspiration for the **Dogs Helping Pets (DHP)** solution came from posts on Nextdoor. I live in a neighborhood comprised of animal enthusiast - from dogs and cats to peacocks. Most  posts involve lost cats or dogs, and there tends to be much involvement from the community to reunite owners with their pets. Neighbors volunteer their time to take walks looking for other's lost pets. They take pictures of random cats in the neighborhood and reply to a Lost Pet post, asking "Is this him?" Knowing that many of the people in my community are dog owners and are willing to dedicate some of their time, I asked... How much are they willing to do?

There already exists the idea of Pet Detectives that use trained search and rescue dogs to track or trail lost pets. Many of these organizations are paid experts with well trained dogs. However, it is my hope that an online application, can be developed to grow a larger network of trained dogs and connect them with owners of lost pets in the community.

#### Examples of Related Networks or Systems
There are examples of professional search and rescue services for lost pets. These often come with a high fee, anywhere from a few hundred dollars or more.

**Dogs Finding Dogs** is a non-profit organization located in Baltimore and dispatches trained tracking teams to search for lost animals (http://articles.chicagotribune.com/2012-10-03/features/sc-fam-1002-dog-track-20121002_1_pet-detectives-cats-and-dogs-gps-collar).

**K-9 Search and Rescue of Orange City** is another organization that started in California but has opened services to Central Florida. Most cases K-9 Search and Rescue is contracted for invloves missing persons and criminal cases. However, in 2013 the organization expanded to include missing pets. According to a news article released by West Orlando News, the number of Pet Detectives across the country is relatively small.(http://westorlandonews.com/local-pet-search-rescue-service-offered-locally/).

**Home Again** is an online community and service that supports reuniting lost pets with their owners. Although the service does include access to an online community network and resources for search and rescue dogs, it's main focus is to offer micro chipping services as a preventative measure (https://www.homeagain.com/).


#### Limitations
The distinction between the Dogs Helping Pets (DHP) network and others is that DHP is a volunteer based service. With this comes a few limitations and assumptions:

> - The system will only be effective if we have community buy-in, both by owners of lost pets and potential trainers
> - The success rates of finding lost pets through community trained dogs is dependent on trainer effort
> - This system can quickly become unbalanced with a high owners of lost pets to available trainers ratio and should be considered

## Requirements

The DHP network includes an online application that can be used by two types of users in the community, owners of lost pets and dog owners who serve as trainers. The application has two goals: 

1. Provide resources for dog owners who wish to train their dogs to be better trackers for purposes of locating lost pets in their community
2. Serve as a communication tool to connect owners of lost pets with owners of trained tracking dogs

Inputs to the system include user discussion posts which should have the function to add, edit and delete. Most importantly is the ability to effectively connect owners of lost pets with owners of trained dogs. Status indicators or badges should be shown next to usernames in the system to identify individual roles in the network. These roles are not mutually exclusive. In other words, a dog owner of a trained dog can have an additional lost pet and so both status indicators should be visible by the online community. 

As the network grows, outputs to measure the effectiveness of the system should be included. For example, tracking how many pets were successfully reunited through an owner of a trained dog can serve as a way to advertise expertise and increase participation.

## Dogs Helping Pets Network Model

The links below will direct to pages that describe the DHP Network model at different levels of detail. These diagrams are used as a guide to decribe the elements in the application how they function together.

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components in the DHP Network
* [**Class Diagram**](model/class_diagram.md) - provides details of objects in the system and their attributes
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of how objects in the system interact

## Dogs Helping Pets Network Simulation

(remove: for part 3 add two to three sentences here and link the [**(your own name)**](RStraney/model/README.md) file in the analysis folder - which describe how you would simulate this - type of simulation, rough details -inputs, outputs - how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)
It is important to simulate user data to test functionality of the system as well as effectiveness. Once the DHP Network is built, a small database of test user cases can be created to run through the system. Details of how a simulation can support development for this model can be found **here** (model/README.md). 
System functions associated with users, like credential verification, adding and deleting discussion posts and status indicators (owner of a lost pet, dog trainer or both) can be tested for proper functionality. A more challenging problem is the question of how stable a network like this can be if there are not a balanced number of dog trainers to owners of lost pets. A more complicated simulation can be constructed which would evaluate how the system is used based on user behavior (i.e. people with lost pets discontinue using the application because there are not enough owners of trained dogs).

## Dogs Helping Pets Network Framework
An initial Python program has been developed as a foundation for the DHP Network application. The program was written following the Object, Class and Behavior Diagrams mentioned above.

[**DHP Network Code**](code/README.md)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
