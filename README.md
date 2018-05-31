# Airport Concierge
2-Day Workshop to create a robot concierge at the Airport

## Overview of Product
The vision of the product is to provide a more engaging customer experience at an airport using the robot.

- Customers will be able to purchase tickets directly from the robot (providing they have pre-registered)
- Customers will be able to checkin and receive their boarding pass (via email) from the robot
- Customers can ask the robot for directions around the airport as well as general information such as flight arrivals/departures, weather, train timetables (need API key), etc
- The robot will also monitor security by screening checkins
- Employees can also use the robot to leave messages for each other, perhaps this is another robot in a secure area where employees have no access to mobile phones

## Setup
Workshop will be split into 2 teams of 4.

There are 4 components, 1 per team member, that will need to be developed to complete the product as a whole. There will be a level of integration required between some of the components.

Requirements for each of the components will be provided. They may be vague and contradictory so it will be necessary for the team to work together and clarify the requirements with the Product Owner and/or Technical Lead.

## Components

The 4 components are:
- Ticket Purchase
- Boarding Pass
- Directions/Information
- Security/Employee

### Ticket Purchase
Tickets can be purchased from the robot once the customer has pre-registered via a dedicated site leaving their name, email and credit card details. When pre-registering they receive a Nao Mark that is their personal robot identifier. This Nao Mark is shown to the robot when purchasing the tickets which will draw the customers' registered details from its database.

### Boarding Pass
The Boarding Pass is a digital one. It will consist of a unique Nao Mark and the customer's photo. The customer will receive a boarding pass via email to the address they pre-registered.

### Directions/Information
Customers can ask the robot directions to locations around the airport such as toilets, gates, restaurants, bars, etc. The robot will use voice and gestures to do so. Customers can also ask questions about things like the weather at their location as well as their destination. They can ask for the scheduled arrival and departure times of flights and the timetable for trains departing the airport.

### Security/Employee
When a customer's boarding pass is scanned the robot performs a security check to see if the customer is listed and if so sends an alert to the security team. Additionally, the robot will also be a time clock device for employees to clock in and out when they start and finish work. Employees can also leave voice messages for each other.

## Code Repository
All code will be stored in GitHub (**ADD LINK**)

## Requirements
Requirements will be in the form of GitHub Issues labelled as `enhancement`

## Bugs
Bug reports will be in the form of GitHub Issues labelled as `bug`

## Test Cases
Test cases will be stored in the GitHub repository. They will use Markdown and use the following format:

Step | Description | Expected Result | Actual Result | Pass/Fail | Issue
---- | ----------- | --------------- | ------------- | --------- | -----
1   | User shows robot Nao mark | Robot recognises mark and takes appropriate action | Robot does not recogise Nao mark | **FAIL** | [22](link-to-issue)


## Development Lifecycle
The lifecycle will run something like...
1. Candidate designated as the Developer analyses the requirements and produces a high level design (1 page, pictures encouraged). Team discussion encouraged.
1. The Developer develops their component in Choregraphe (or Python is capable) making use of the supplied libraries that have already been developed.
1. The Developer unit tests their component and declares it ready to be integrated
1. The code is integrated into the releasable product and it is ready for testing
1. Another candidate will be assigned as Tester writes test cases, using supplied Excel template, based on the provided requirements (or clarified requirements)
1. The Tester executes the test cases they have written and raises Bug Issues in GitHub for any bugs they discover
1. The Developer fixes those Bug Issues raised and it is re-tested
1. The cycle continues until the product is considered DONE or time available has expired

