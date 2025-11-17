# LEETCODER

## Background
Regardless of experience, anyone who works with technology can benefit from understanding the 1st principles upon which it operates. This has become more important with the increased usage of LLM's to accelerate development because software engineers' value will increasingly come from their ability to solve novel, complex problems. This hypothesis is inferred from how other industries have evolved after technology's introduction replaced some portion of the workflow.

For example, the industrial revolution introduced the assembly line which converted a large portion of the workforce from agriculture to manufacturing jobs. When technology was introduced, much of the "work" as it was previously defined was replaced by computers. Examining the situation in greater detail, it becomes clear that the what was replaced were easy to understand, clearly defined, repetitive tasks. This is where computers excel. Automation requires these criteria. Interestingly, the jobs did not all disappear. Instead, remaining workers were forced to focus on solving more abstract problems requiring greater understanding of 1st principles, problem solving, industry dynamics, and communication. Essentially, workers remaining moved up a level of abstraction in their day to day work. Now, they had to work on the systems, processes, and machines that delivered value instead of doing the value themselves.

My conjecture is that a similar transformation will happen with technology workers. Instead of coding being the primary job function, solving problems about the systems, processes, and machines doing the coding will become the job. To do this, people will need to understand the 1st principles of computation, problem solving, mathematics, data, and computer science. Essentially, we must become experts quantiative computational problem solvers.

Thus, I am creating LeetCoder to help people make this transition ahead of their peers. LeetCode with ~3,000 questions which tech companies have used to hire candidates provides a good starting point for finding the most valuable knowledge and skills to the industry. Those who become top 10% experts in solving these problems will become the most sought after workers in the future. They will be creating the change that everyone else will be trying to keep up with.

## Problem
What is the most efficient way to master LeetCode?


## Solution
Given a set of 3,000 computation problems, discover the hidden pattern in them that allows anyone to solve all the problems.

Constraints
    - Avoid brute force because:
        - Most people who will do LeetCode problems are likely looking for employment. Thus, they will only want to prepare for 1 month or 30 days. Solving the current 3,000 problems in 30 days would requiring solving 100 problems daily. Assuming each problems when first encountered requires 30 minutes to solve adn there are 24 hours in a day, the theorectical limit on the maximum problems which can be solved daily is 48.
        - Also, the total number of problems was ~1,500 in 2000. If this rate can be assumed to be consistent, then ~300 new problems are added a year or ~1 question daily. This simple analysis reveals that not only is brute force not an option but the value of a system reducing the LeetCode problem space increases in value over time.
        - Connecting this back to the Background section. My conjecture is that the value of such a LeetCode mastery system will likely be exponential over the next 10 years as LLMs commoditize writing code increasing the need to solve the problems to complex for it to tackle. Thus, creatively building upon the data structures and algorithms used to solve LeetCode problems will increasingly become the job of software engineers.

    - Use python:
        - We should treat python as pseudocode. It's simple syntax and lack of types is an advantage during early problem solving where the goal is to learn as much as possible quickly to precisely define the problem before starting to work.

    - Follow a simple process:
        1. Define the problem in your own language to start understanding the true problem beneath the problem.
        2. What is the input?
        3. What is the output?
        4. Are there other givens?
        5. What features of the problem may be used to group similar problems in the future? Add them as tags to the question.
        6. What are your initial 3-5 ideas about the problem?
        7. What actions performed on the input results in the output in 3-5 steps? (mapping the problem to the solution)
        8. What are the major potential phases/states of the problem? input = nothing, input = something, input = unexpected -> next branches from here -> next from here, etc
        9. How would you restate this mathematically?
        10. How can the math equation be decomposed into input -> process -> output at the highest level?
        11. How can we restate our problem in the problem-solution-behavior domain space such that we can solve it from the output working backwards?
        12. How can the problem now we separated into 3 layers? Layer 1 is the axiomatic layer which is where declarative pure functions operate on data directly to transform it. Layer 2 is the internal declarative semi-pure funcational layer where higher order function (HOF) focus on transforming our functions so that any valid completed code is never refactored, removed, or lost. Layer 3 is the chaotic imperative layer where functions optimized for low latency execution are layered as needed with each other to facilitate adaptive response to unforeable states that may be encountered. This is our sensory layer. It is the largest. It is the most likely to break. It is the most likely to encounter malicious action. Thus, it's job is to never allow anything to pass through to any other part of the system and never go down itself.
        13. How do we generalize feedback across these layers to increasingly automate key functionality?

## Approach

1. Do 10 LeetCode problems to personally understand the LeetCode problem-solution-behavior domain space.# leetcoder
