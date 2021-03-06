# Personalized High School Math Exercises Recommendation based on Knowledge Graph Completion and Knowledge Tracing

## Introductio$$

$$n

In the context of the popularity of artificial intelligence technology, AI has become a trend in various industries. The theoretical breakthrough has brought about large-scale commercial applications and profoundly changed social development. 

When it comes to AI-education, although there are many deep learning and artificial intelligence solutions, there are not many projects that can be applied and implemented in practice. Most of the solutions are still in the conceptual stage or data collection stage, which is far from practical application. 

In recent years, domestic adaptive learning has begun to enter the field of vision of many people engaged in education training and education investment. There are more and more educational technology companies focusing on adaptive learning tools in the market. At the same time, many educational companies have begun to use adaptive learning as the main core function or main selling point of their products. The biggest advantage of adaptive education is that it can locate the knowledge loopholes of each student. The adaptive learning platform will guide the student to the next learning content and activities most suitable for him. When the student encounters a course that is too difficult or too low during the learning process, the difficulty of the course can be automatically adjusted. Teachers can also analyze the knowledge gaps of each student according to the learning status evaluation report provided by the system, and adjust the learning progress in real time to provide personalized teaching for each student. So in theory, adaptive learning is one of the potential feasible solutions to the problem of "teaching students in accordance with their aptitude" in online education. To make an practical adaptive learning system, I plan to adapted Knowledge Graph (KG) technique with knowledge completion and knowledge tracking in making such a recommendation system.

The key challenges include building one knowledge graph, performing knowledge completion and building recommendation model. 

In the education industry, AI technology is mainly used for the recommendation of teaching resources to teach students in accordance with their aptitude. However, the current AI-based teaching is still at a simple stage, and coarse-grained recommendation algorithms are used to push teaching resources in batches, causing a lot of burden. Compared with other methods, the knowledge graph can express the relationship between knowledge more widely and intuitively. The push based on knowledge graph can ensure better domain adaptability, knowledge granularity and construction automation.

However, the problem of missing ternary groups (i.e., missing links) is common in knowledge graphs. Because the size of missing ternary is usually large, it is costly to find these ternary manually. Therefore, researchers have designed the Knowledge Graph Completion task, which aims to automatically complete missing ternary groups through machine learning models. This task is also known as Link Prediction because it does not add new entities or relationships, but completes links between existing entities. The knowledge graph completion algorithm can make the knowledge graph more complete, which is currently a research hotspot in the field of artificial intelligence. It predicts the missing part of the triples, so that the knowledge graph becomes more complete. Based on the existing knowledge graph completion algorithm, combined with the particularity of education data, we optimized the model construction budget method. 

Knowledge Tracing is a technique for modeling a student's knowledge based on past answers to obtain a representation of the student's current knowledge state. In order to make personalized question recommendations based on student learning, knowledge tracing algorithms are needed to measure individual student learning, and in this paper we propose an improved knowledge tracing approach to better model the learning cognitive model for better performance.

First we build a knowledge map for high school mathematics education based on the existing dataset of public high school mathematics questions, and work at this stage includes entity extraction, relation extraction and attribute extraction, and knowledge fusion techniques. Then we try to use a variety of knowledge graph complementation techniques to complement the knowledge graph and propose an improved knowledge graph complementation algorithm, complete theoretical design, algorithm optimization and experimental validation, and analyze and compare with the existing knowledge complementation models.

Then we complete the design, optimization and experimental validation of the improved knowledge tracing algorithm for high school mathematics education knowledge, and compare it with existing Bayesian-based knowledge tracing and deep knowledge tracing models. And compare it with other cognitive model inference algorithms such as cognitive diagnostics.

Finally, a recommendation model for high school mathematics questions is implemented based on complementary knowledge mapping and knowledge tracing models. A high performance recommendation model based on the high school mathematics knowledge model is proposed to complete the theoretical justification, model optimization and experimental validation.
## High School Math

### Definitioin of Subject Knowledge 

Disciplines and knowledge are closely related to each other, so that disciplinary knowledge denotes the specific knowledge contained in a particular field of study. Disciplines are referred to in this study only for specific subjects in the field of education, such as mathematics, language, chemistry and so on. The first step is to learn how to make the best use of the knowledge that is available. The knowledge is obtained from practice, so after learning it, it can also be applied to social practice. Scientific knowledge is declarative because it can be expressed in a series of symbols, words and diagrams; it is also procedural because it can be arranged and learned according to a specific logical order in the process of concrete learning.

Mathematics is a science specializing in the study of the relationship between quantities and spatial forms, its symbolic system is more complete, the formula structure is clear and unique, text and images and other expressions of language is also more vivid and intuitive.

### Knowledge structure of High School Math

The knowledge that learners need to learn mostly comes from the summaries of the experiences of their predecessors in practical activities. The learning process is a process of cognitive learning of the summarized knowledge and continuous digestion, adjustment and reorganization of the knowledge structure, so as to build a more perfect and suitable knowledge structure, as well as a process of integration with innovative thinking. 20], so a good cognitive structure can promote the formation of knowledge structure, and a good knowledge structure can enrich the organization form of cognitive structure. Since the disciplinary knowledge structure consists of two parts: knowledge composition and knowledge dependency, we will analyze the disciplinary knowledge structure from these two aspects.

#### Knowledge composition

Knowledge composition refers to the organization of knowledge within a subject area, which mainly includes knowledge points, knowledge blocks and knowledge systems.

- knowledge point: A point of knowledge is the smallest constituent unit of the knowledge structure of a discipline and is used to represent specific concepts.
  propositions, formulas, etc.
- knowledge block: A knowledge block is a collection of one or more sets of knowledge points, also known as knowledge modules, in which knowledge blocks and knowledge blocks can be combined to form new knowledge modules, and a subset of knowledge blocks is called a knowledge sub-module
- knowledge body: a body of knowledge is a structured system that is a combination of all the pieces of knowledge in a particular subject area.

#### Knowledge Relation

Knowledge relations represent the connections between knowledge points (or between knowledge blocks and knowledge chunks) in the discipline knowledge structure. It is through these connections that different knowledge points can be formed into knowledge blocks, and different knowledge blocks can be combined to form the whole disciplinary network knowledge structure system. There are many different kinds of knowledge relationships, so that different definitions of knowledge relationships lead to different knowledge structures. Therefore, in order to unify the definition of knowledge relations, we divided them into general relations and special relations based on the general and special characteristics of discipline knowledge structure. The special relationships represent the unique knowledge relationships of a particular discipline, while the universal relationships represent the general relationships of any discipline. Secondly, according to the demands of knowledge mapping research, we divide universal relations into six kinds of knowledge relations: synonymous, fraternal, antecedent, consequent, inclusive and antagonistic; and special relations into four kinds of knowledge relations: detailed, transformative, causal and correlative.

- tautology: Expresses the relationship between two points of knowledge that have the same meaning as what is being described, e.g. regular and equilateral triangles.
- fraternity: Expresses the relationship between two knowledge points that have the same parent class

- predecessor: It means that you need to finish learning knowledge point A before learning knowledge point B, that is, A → B is a precursor relationship.
- successor: denotes the inverse of the antecedent relationship, i.e., B→A is the successor relationship.
- containment: Indicates that knowledge point B is included in the definition of knowledge point A, i.e., A → B is an inclusion relationship.
- antagonism: From a certain point of view, knowledge point A is incompatible with knowledge point B, i.e. A↔ B is an antagonistic relationship
-  refinement: A grammatical analysis of the definition of knowledge point A leads to knowledge point B, where A↔ B is a detailed relationship
- transformation: denotes that knowledge point A and knowledge point B can be transformed to each other under certain conditions, i.e., A↔ B is a transformation relationship.
- causation: denotes that knowledge point A can be deduced from knowledge point B as a known condition, i.e., A↔B is a causal relationship
- relation: Indicates that there is a relationship between the definitions of Knowledge Point A and Knowledge Point B, but the relationship is not explicitly specified, i.e., A↔ B are correlated.

In the process of constructing the discipline knowledge structure, firstly, we need to analyze the current discipline knowledge content, teaching objectives, teaching objects, teaching strategies and discipline characteristics in detail; secondly, we divide the whole discipline knowledge system into several knowledge modules, and then we divide each knowledge module into several knowledge points; finally, with reference to the above ten kinds of knowledge relationships and the knowledge relationships extracted from data sources, we can determine and establish the relationships between knowledge modules and knowledge modules, between knowledge modules and knowledge points, and between knowledge points and knowledge points, so as to form a complete discipline knowledge system structure.



### The property of High School Math

Mathematics is a science that specializes in the relationship between quantity and spatial form. Its symbol system is more complete, the formula structure is clear and unique, and the language of expression such as words and images is more vivid and intuitive. The knowledge structure of senior secondary mathematics is a more logical and systematic knowledge system organized on the basis of the knowledge structure of junior secondary mathematics. This is because learning for any discipline needs to be based on the existing cognitive structure in order to progressively effective learning and skills training, so in the process of learning high school mathematics, you need to have a solid foundation of junior high school mathematics discipline knowledge. In the past few years, there have been a number of cases in which the students have been able to learn from each other.

- Highly abstract

  Mathematics has a high degree of abstraction, because the discipline's knowledge system is built using many abstract knowledge concepts, and with the help of these concepts and knowledge to learn and expand thinking, forming new abstract conceptual knowledge. The abstraction of mathematics is reflected in the object is not concerned with the introduction of specific content, only the number of relationships between the spatial form. Therefore, abstraction in mathematics is different from abstraction in other disciplines in terms of both object and degree. There are also some differences between mathematics and the natural sciences, because in mathematics the accuracy of calculations, proofs, and inferences can only be verified using rigorous logical methods and cannot be tested by repetitive experiments, whereas in the natural sciences the verification is the opposite.

- strict logic

  The discipline of mathematics is very logical because any conclusion reached in mathematics requires rigorous logical reasoning and rigorous proof in order to be considered reasonable. However, mathematics is not the only discipline that possesses rigorous logic; other natural science studies of reasoning and proof must also possess a certain degree of logic. In mathematics, not all conclusions reached after reasoning and proof can be applied in practice, because many mathematical models are developed and mathematical conclusions drawn under ideal circumstances.

- Broad applicability

  Mathematics is an important means and tool for us to participate in practical social activities or scientific research, and the study of mathematics is indispensable in all walks of life and in all areas of society. Therefore, mathematics has a wide range of applications and has become an important basis for the development of modern science.


## Knowledge Graph
Knowledge graph itself is a logical hierarchical structured knowledge graph, and the formation of knowledge graph requires relevant construction techniques. Therefore, the architecture of the knowledge graph includes the logical structure and technical structure (or architecture) of the knowledge graph.



#### Logical

The knowledge graph logically consists of a data layer and a schema layer. The data layer is used to store factual data, i.e., knowledge information. In the process of visualizing the knowledge graph, the data storage format of ternary group is usually used to express facts or knowledge information. The ternary knowledge information is generally stored in a graph database (a kind of NoSQL database), such as the open source Neo4j, FlockDB by Twitter and GraphDB developed by Sones, etc. The schema layer is used to manage knowledge information. The schema layer is the core architecture built on top of the data layer to manage the knowledge graph, and it usually uses an ontology knowledge base to effectively manage the knowledge graph. Building a knowledge graph through ontology knowledge base not only strengthens the hierarchical structure of the knowledge system, but also reduces the redundancy of knowledge information.



#### Technical

The technical architecture of a knowledge graph generally refers to the architecture of the relevant technologies used in the construction of the knowledge graph and its application. The dotted box shows the specific process of building a knowledge graph and its updating. The construction process of knowledge graph starts from the collection of data sources (unstructured, structured and semi-structured data), using automation, semi-automation and other technical means to extract the research-related knowledge information (including the extraction of knowledge entities, relationships and attributes) from data sources and third-party databases, and then store these knowledge information in a certain logical order into the The knowledge graph is then built into the database. Then, after a series of operations such as knowledge representation, entity alignment, ontology construction, knowledge update and knowledge inference, the knowledge graph can be constructed.

The knowledge graph can be constructed in two ways: bottom-up and top-down. Bottom-up means extracting highly reliable knowledge entities from some open data links and adding them to the ontology knowledge base, and then designing and implementing the top-level ontology of the knowledge graph. The top-down construction method is to define the required knowledge ontologies and data storage forms on the basis of the existing knowledge base, and then store the knowledge entities into the ontology knowledge base one by one. It is found that bottom-up knowledge graph is the most widely used knowledge graph construction method, the most representative applications are the Knowledge Vault designed and developed by Google and the Satori knowledge base designed and built by Microsoft.


## Data Tracing 
Knowledge tracking is a key issue in personalized tutorials, characterized by automation and personalization, with the task of automatically tracking the evolution of students' knowledge levels over time based on their historical learning trajectories so that they can accurately predict how they will perform in future learning and provide appropriate learning support. In this process, the knowledge space is used to describe the set of knowledge mastered by students, and some educational researchers argue that the exercises will test a specific set of related knowledge points, and students' mastery of the knowledge points examined in the exercises will affect their performance on the exercises, i.e., the set of knowledge mastered by students is closely related to their extrinsic performance on the questions.

### Problem 
The knowledge tracking task can be summarized as follows: given a sequence of observations of a student's performance on a particular learning task $x_0,x_1,...,x_t$ , and predict their performance on the next one $x_{t+1}$. The diagram below depicts a visual display of a student's knowledge tracking in an 8th grade math classroom. This student started with two correct answers to a question about square roots, then incorrectly answered a question about the X-axis intercept, followed by a series of questions about the X-axis intercept, the Y-axis intercept, and graphing linear equations (where square roots, the X-axis intercept, and the Y-axis intercept can all be considered as a knowledge point). As the student finishes each exercise we can predict how he will perform on the next topic, which can be a topic from a different knowledge point. In this figure we only predict mastery of the knowledge points that are relevant to the current exercise.
![](./figs/fig1.png)


Bayesian Knowledge Tracking (BKT) is the most popular model of knowledge tracking. In the BKT model a hidden variable is proposed about the knowledge state of the student, which is represented by a binary group {mastered that knowledge, did not master that knowledge}. The whole model structure is actually an HMM model that predicts the next state based on the state transfer matrix and the student's answer results based on the current state. And in the BKT model it is believed that once knowledge is mastered it is not forgotten. And the current work also introduces the probability of guessing the question correctly if the student does not have the knowledge and the probability of answering the question incorrectly if the student has the knowledge, the student's prior knowledge and the difficulty of the question to extend the model. However, with or without these extensions, several problems remain with the BKT model.

- It is not practical to represent students' state of knowledge in binary groups.

- The mapping between hidden states and practice doing questions is vague, making it difficult to adequately predict a concept for each exercise

- The binary representation of the observation state will limit the type of topic

　　Recurrent neural network is a time series model where information is propagated recursively based on earlier information and current input. Compared to HMM, RNN has high dimensional, continuous hidden state representation.The biggest advantage of RNN is that it can exploit more early information, especially the LSTM network structure, which is a variant of RNN.RNN has achieved very good results on many time series problems, so it may be better to apply RNN to knowledge tracking.

　　Here we can use either the traditional RNN or the LSTM model. Before we enter the data into the model we need to convert the input data into a vector representation (the input data is the result of the questions we observed the students doing). The vector representation of the input values can be used in two ways.


- One-hot representation.  The total length is 2M (note that the whole model is only concerned with the knowledge points to which the topic belongs, and the result of doing the question). one-hot representation is more convenient, but once the number of knowledge points is very large, the vector will become high-dimensional and sparse.
- Compress the high-dimensional sparse input data into the low-dimensional space (log2Lu_1D440 ) by the compression-aware algorithm.

　　The output result 𝑡 is a vector of length M. Each value in the vector describes the probability of mastery of the corresponding knowledge point (or the probability of answering the question under the corresponding knowledge point correctly). Thus, the entire sequence is a prediction of the mastery of each knowledge point at step 𝑖 based on information from the first 𝑖-1 time step.

　　The loss function of the model is:

$$\mathcal{L}=\frac{1}{\sum_{i=1}^{n}\left(T_{i}-1\right)}\left(\sum_{i=1}^{n} \sum_{t=1}^{T_{i}-1} l\left(\mathbf{y}_{t}^{i} \cdot \delta\left(q_{t+1}^{i}\right), a_{t+1}^{i}\right)\right)$$






### Survey
#### Deep Knowledge Tracing and Dynamic Student Classification for Knowledge Tracing
Tracking a student's knowledge state during the learning process has been studied in Intelligent Tutoring Systems (ITS). In order to provide more supportive learning instructions, we propose a new knowledge-tracking model. In this paper, we propose a novel knowledge-tracking model that: i) captures students' learning abilities and dynamically assigns them to different groups with similar abilities at fixed time intervals; and ii) combines this information with a recurrent neural network architecture called deep knowledge tracking. The experimental results confirm that the proposed model is significantly superior to known state-of-the-art techniques for student modeling in predicting student performance.

![](figs/studenttracing.png)

#### AKT


#### Factorization Machines for Knowledge Tracing
Knowledge tracing is a sequence prediction problem where the goal is to predict the outcomes of students over questions as they are interacting with a learning platform. By tracking the evolution of the knowledge of some student, one can optimize instruction. Existing methods are either based on temporal latent variable models, or factor analysis with temporal features. We here show that factorization machines (FMs), a model for regression or classification, encompasses several existing models in the educational literature as special cases, notably additive factor model, performance factor model, and multidimensional item response theory. We show, using several real datasets of tens of thousands of users and items, that FMs can estimate student knowledge accurately and fast even when student data is sparsely observed, and handle side information such as multiple knowledge components and number of attempts at item or skill level. Our approach allows to fit student models of higher dimension than existing models, and provides a testbed to try new combinations of features in order to improve existing models. 
On the Assistments 2009 dataset:

| Model                                  | Dimension | AUC       | Improvement |
| -------------------------------------- | --------- | --------- | ----------- |
| KTM: items, skills, wins, fails, extra | 5         | **0.819** |             |
| KTM: items, skills, wins, fails, extra | 5         | 0.815     | +0.05       |
| KTM: items, skills, wins, fails        | 10        | 0.767     |             |
| KTM: items, skills, wins, fails        | 0         | 0.759     | +0.02       |
| (*DKT* (Wilson et al., 2016))          | 100       | 0.743     | +0.05       |
| IRT: users, items                      | 0         | 0.691     |             |
| PFA: skills, wins, fails               | 0         | 0.685     | +0.07       |
| AFM: skills, attempts                  | 0         | 0.616     |             |

On the [Duolingo](http://sharedtask.duolingo.com/) French dataset:

On the [Duolingo](http://sharedtask.duolingo.com/) French dataset:

| Model                        | Dimension | AUC       | Improvement |
| ---------------------------- | --------- | --------- | ----------- |
| KTM                          | 20        | **0.822** | +0.01       |
| DeepFM                       | 20        | 0.814     | +0.04       |
| Logistic regression + L2 reg | 0         | 0.771     |             |



![](figs/factorial.png)



#### DKVMN
Dynamic Key-Value Memory Networks for Knowledge Tracing (abbreviated DKVMN), was proposed in 2017 by Jianshe Shiu of the Chinese University of Hong Kong. Based on the strengths and weaknesses of BKT and DKT and utilizing memory-enhanced neural networks, Dynamic Key-Value-to-Memory Networks (DKVMN) is proposed.
![](figs/DKVMN2.png)

It draws on the idea of memory-enhanced neural networks, combining the strengths of BKT and DKT. DKVMN uses a static matrix key to store the entire knowledge and a dynamic matrix value to store and update the student's knowledge state. In the DKVMN paper, they compared DKVMN and DKT, as well as a complex version of BKT, BKT+. They found that DKVMN achieved excellent performance and was the most advanced model in the KT domain. In addition to the improved performance, it has several remaining advantages over LSTM, including prevention of overfitting, a smaller number of parameters, and automatic discovery of similar exercises after potential concepts.

![](./figs/DKVMN_architecture.png)
#### End-to-end (2018)
Existing DKT requires human labeling that show the required skills to solve a question, which limits the capacity of the model and application to real-world data. Someone propose an end-to-end DKT model, which does not depend on any human labeling. Regarding the process of translating questions into tags as reducing the question-space dimension by a binary embedding matrix by introducing a new Q-Embedding Model.
![](./figs/q-embedding.png)
In order to learn the question-embedding matrix $P$, we introduce the Q-Embedding Model. We present the architecture of the model in Figure 1. In the the Q-Embedding Model, a student’s question-answer logs are directly used as the model’s input $x_t$, and the output $y_t$ is the predicted probability of the student answering each question correctly the next time. In addition, to learn the matrix that translates input question-space to low-dimensional tag-space, we add two hidden layers: $u_t$ and $v_t$ with a size of $2N_0$ and $N_0$ , respectively. Here, $N_0$ is the dimension of the tag-space and $P$ is a sigmoid-activated matrix with a size of $M \times N_0$. After training the model, we extract $P$ and binarize it to 0 and 1 on a certain condition. In addition to the DKT’s objective function $L_p$ in equation 1, in order to learn a better questionembedding matrix, we introduce two objective functions in the following equation:

$$L_{r}=\sum_{t} l\left(\mathbf{x}_{t}^{\prime T} \tilde{\delta}\left(\mathbf{q}_{t}\right), \mathbf{a}_{t}\right)$$

$$L_{s}=\sum_{t}\left(0.5-\left|\mathbf{u}_{t}-0.5\right|\right)$$

#### Prerequisite-Driven Deep Knowledge Tracing
Penghe Chen et al. take into account the sparsity of the data when using DKT (the SKILL space is larger and students are more limited in doing the questions), and to solve the inaccurate model evaluation due to the sparsity of the data, they propose to incorporate information about the knowledge structure into the model to solve the above problems, specifically to consider the before-and-after relationship of incoming knowledge.
The core idea is that:
If $K_1$ is the antecedent of $K_2$ 


$$\begin{array}{l}
\max _{\Theta} \log \prod_{i} \prod_{t} P\left(y_{i, \pi(i, t), t} \mid \mathbf{s}_{i}, \Theta\right) \\
\text { s.t. } P\left(m_{i, k_{2}, t_{2}}=1\right) \leq P\left(m_{i, k_{1}, t_{1}}=1\right) \\
\forall\left(k_{1}, k_{2}\right) \in E \& y_{i, \pi\left(i, t_{1}\right), t_{1}}=y_{i, \pi\left(i, t_{2}\right), t_{2}}
\end{array}$$


#### Towards an Appropriate Query, Key, and Value Computation for Knowledge Tracing

Knowledge tracing, the act of modeling a student’s knowledge through learning activities, is an extensively studied problem in the field of computer-aided education. Armed with attention mechanisms focusing on relevant information for target prediction, recurrent neural networks and transformer-based knowledge tracing models have outperformed traditional approaches such as Bayesian knowledge tracing and collaborative filtering. However, the attention mechanisms of current state-of-the-art knowledge tracing models share two limitations. Firstly, the models fail to leverage deep self-attentive computations for knowledge tracing. As a result, they fail to capture complex relations among exercises and responses over time. Secondly, appropriate features for constructing queries, keys and values for the self-attention layer for knowledge tracing have not been extensively explored. The usual practice of using exercises and interactions (exercise-response pairs), as queries and keys/values, respectively, lacks empirical support.

In this paper, we propose a novel Transformer-based model for knowledge tracing, SAINT: Separated Self-AttentIve Neural Knowledge Tracing. SAINT has an encoder-decoder structure where the exercise and response embedding sequences separately enter, respectively, the encoder and the decoder. The encoder applies self-attention layers to the sequence of exercise embeddings, and the decoder alternately applies selfattention layers and encoder-decoder attention layers to the sequence of response embeddings. This separation of input allows us to stack attention layers multiple times, resulting in an improvement in area under receiver operating characteristic curve (AUC). To the best of our  knowledge, this is the  first work to suggest an encoder-decoder model for knowledge tracing that applies deep self-attentive layers to exercises and responses separately. We empirically evaluate SAINT on a large-scale knowledge tracing dataset, EdNet, collected by an active mobile education
![](./figs/premodel.png)

![](./figs/themod.png)
### Model

### Evaluation