
# infrastructure as code
- review
- mutualization

idempotence (synchronisation of config and servers)

versionning
-> allows to track the changes
-> easier to rollback changes to a previous working configuration in case of a problem.

-> visibility
-> reusability
- consistency
confidence that all the machinse have the same configuration

pitfalls

continuous integration ??

-deliver small changes frequently
- continuously synchronize (or even continuously rebuild) to ensure consistency
avoid The Automation Fear Spiral

pipelines
Kief Morris suggests to dissociate
- global infrastructure pipeline
- image pipelines
- service pipeline (including database and application, may include generating VMs)

in other words avoid monolith pipeline, use a modular infrastructure

*GOTO 2016 • Implementing Infrastructure as Code • Kief Morris*

## testing 
Kief Morris suggests
server expect ? a ruby library (not found)
https://github.com/test-kitchen/test-kitchen

## secrets

keys may be stored crypted in a repository

## getting started

*The only way to break the spiral is to face your fears. Pick a subset of your servers, choose one or two things on them to put under configuration management, and then schedule these to be applied unattended, at least once an hour.*

*Starting small and simple helps to limit the risk. The important thing is that you take the leap—let the automation go on its own, without you holding its hand. Then you can increase the scope—add a few more parts of the server to the automation, and extend it to more servers.*

*You should also build out other things that will give you more confidence, piece by piece. Add monitoring to detect when the thing you’ve automated goes wrong. Set up Continuous Integration to automatically test the configuration change every time you commit. Again, getting these pieces in place with a small, simple set of configuration, creates the platform. You can then extend the coverage with confidence.*

*(https://www.thoughtworks.com/insights/blog/infrastructure-code-automation-fear-spiral)*

## resources
https://www.thoughtworks.com/insights/blog/infrastructure-code-reason-smile
https://www.thoughtworks.com/insights/blog/infrastructure-code-automation-fear-spiral

