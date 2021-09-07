# Rasa Action Examples

<img src="example-icon.png" width=150 height=150 align="right">
<img src="square-logo.svg" width=150 height=150 align="right">

This repository contains demonstrations of Rasa custom actions. These custom actions
might demonstrate how to integrate with a 3rd party but may also show how the Rasa SDK
can be used. The goal is to encourage experimentation and to quickly offer support to
more tools. By hosting these components here they do not need to go through the same
vetting process as the components in Rasa and we hope that this makes it easier for
people to contribute new ideas.

The components in the repository are **not officially supported**. There will be units tests
as well as modest documentation but this project should be considered a community project,
not something that is part of core Rasa.

# How to Use 

Every folder in this project represents a Rasa project. Each Rasa project
contains a custom action that demonstrates something novel. Each project comes with
a `readme.md` file that explains how the custom action works and the goal is to keep
all the examples minimal in nature. They should be just enough to explain a concept
but lightweight enough so that they are easy to copy into an existing Rasa project.

## Existing Examples 

### Fallback Buttons 

The `fallback-button` folder contains a custom action that triggers whenever the NLU fallback is triggered. It will then try to generate buttons with suggestions for the user on what to do next.
