# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2780

    level1["cough"] = - 1.0
    level1["cough_info_gain"] = 0.2364

    level1["radon"] = - 1.0
    level1["radon_info_gain"] = 0.0348

    level1["weight_loss"] = - 1.0
    level1["weight_loss_info_gain"] = 0.0290

    level2_left["smoking"] = - 1.0
    level2_left["smoking_info_gain"] = 0.0
    level2_right["smoking"] = - 1.0
    level2_right["smoking_info_gain"] = 0.0

    level2_left["radon"] = - 1.0
    level2_left["radon_info_gain"] = 0.07290

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.72192

    level2_left["weight_loss"] = - 1.0
    level2_left["weight_loss_info_gain"] = 0.1709

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219

    level2_right["cough"] = - 1.0
    level2_right["cough_info_gain"] = 0.32192

    level2_right["weight_loss"] = - 1.0
    level2_right["weight_loss_info_gain"] = 0.17095

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up construct_tree`
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE ***
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer

# ----------------------------------------------------------------------


def question2():
    answer = {}


    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.4253
    # Infogain
    answer["(b) x < 0.2"] = 0.177
    answer["(b) x < 0.7"] = 0.355
    answer["(b) y < 0.6"] = 0.347

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "x<=0.7"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("x<=0.7")
    A = tree.insert_left("y<=0.6")
    A.insert_left("B")
    C = A.insert_right("x<=0.2")
    D = C.insert_left("y<=0.8")
    C.insert_right("A")
    D.insert_left("C")
    D.insert_right("B")
    B = tree.insert_right("y<=0.6")
    E = B.insert_left("y<=0.3")
    B.insert_right("A")
    E.insert_left("A")
    E.insert_right("C")
    answer["(d) full decision tree"] = tree

    return answer

# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914405

    answer["(f) attr for splitting"] = "Car Type"

    # Explanatory text string
    answer["(f) explain choice"] = "The choice for Car type as the attribute for splitting is based on its Gini index, which is the lowest among all attributes except for ID. Since ID is an identification column and lacks relevance for Gini index computation in this context, it's disregarded. Car type exhibits a lower Gini index compared to Shirt Size, indicating it represents a purer class. Therefore, Car type is deemed a more suitable attribute for splitting the dataset."
    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    c = 'continuous'
    d = 'discrete'
    b = 'binary'
    ql = 'qualitative'
    qn = 'quantitative'
    n = 'nominal'
    o = 'ordinal'
    i = 'interval'
    r = 'ratio'

    c_exp = 'Continuous because each measure can be subdivided into smaller measures continuously.'
    qn_exp = 'Quantitative because its value is held in its numerical value.'
    r_exp = 'Ratio because there is a 0;'

    answer["a"] = [c, qn, r]
    answer["a: explain"] = "Continuous because each measure can be subdivided into smaller measures continuously. " \
                            "Quantitative because its value is held in its numerical value. " \
                            "Ratio because there is a 0; at midnight, the day begins and you cannot go back from it, that would be another day, hence another system of reference."

    answer["b"] = [d, qn, r]
    answer["b: explain"] = "Discrete because a human tool is always discrete, even to the finest of values. " \
                            "Quantitative because its value is held in its numerical value. " \
                            "Ratio because there is a 0; when it is completely dark out, and there is no light you cannot go back from it."

    answer["c"] = [d, qn, o]
    answer["c: explain"] = "Discrete because there are only finite ways of describing light levels. " \
                            "Qualitative because its value is held in a person's judgment, not a number. " \
                            "Ordinal because it is assumed the judgments take the form of 'Dim', 'Bright', 'Very Bright'..."

    answer["d"] = [c, qn, r]
    answer["d: explain"] = "Continuous because each measure can be subdivided into smaller measures continuously (i.e. 0.00000000000023° and so on). " \
                            "Quantitative because its value is held in its numerical value. " \
                            "Ratio because there is a 0; an angle cannot be -5° wide."

    answer["e"] = [d, ql, o]
    answer["e: explain"] = "Discrete because there are only 3 levels. " \
                            "Qualitative because the value is held in a title (or better yet, a metal) and not a number. " \
                            "Ordinal because it describes the order of performance."

    answer["f"] = [c, qn, i]
    answer["f: explain"] = c_exp + " " + qn_exp + ' Interval because a 0 is not present, you can go below sea level; the same analogy applies with the different categorization between Celsius and Kelvin.'

    answer["g"] = [d, qn, r]
    answer["g: explain"] = "Discrete because patients are measured in natural numbers. " \
                            "Quantitative because its value is held in its numerical value. " \
                            "Ratio because there is a 0; You cannot have -1 person."

    answer["h"] = [d, ql, n]
    answer["h: explain"] = "Discrete because you cannot have a fraction of an ISBN. " \
                            "Qualitative because the value is held in an identifier. " \
                            "Nominal because there is no inherent hierarchy or other operation, aside from equality and inequality, that can be made on it."

    answer["i"] = [d, ql, o]
    answer["i: explain"] = "Discrete because there are only 3 levels. " \
                            "Qualitative because the value is held in a judgment. " \
                            "Ordinal because it describes the level of light-passing from more opaque to more translucent."

    answer["j"] = [d, ql, o]
    answer["j: explain"] = "Discrete because there is a fixed number of military ranks which cannot be subdivided. " \
                            "Qualitative because the value is held in a rank rather than a number. " \
                            "Ordinal because it describes ranks among military personnel."

    answer["k"] = [c, qn, r]
    answer["k: explain"] = c_exp + " " + qn_exp + " " + r_exp + " When standing right at the center, that is the 0, you can't get closer to the center whilst also being there."

    answer["l"] = [c, qn, r]
    answer["l: explain"] = c_exp + " " + qn_exp + " " + r_exp + " 0 Density is a theoretical value, however I am not sure if it possible. The 0 is present."

    answer["m"] = [d, ql, n]
    answer["m: explain"] = "Discrete because you cannot subdivide a coat check number. " \
                            "Qualitative because the value is held in the identifier. " \
                            "Nominal because it is an identifier, there is no comparison or other operations, other than equality or inequality, to be made."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Model 2 has a better testing accuracy, so it handles better unseen data. Model 1 seems to suffer from overfitting, since the training accuracy is so much higher than the testing accuracy."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Model 2 once more. The measures provided are just the averages of the two datasets' accuracies. Both the models have been trained on Dataset A, so they will always get them right, but Model 2 still has a higher accuracy when it comes to Dataset B, the real unseen data."

    explain["c similarity"] = "Incorporation of Model Complexity"
    explain["c similarity explain"] = "Both MDL and pessimistic error estimate mechanisms are designed to penalize the complexity of a decision tree. They aim to find a balance between the tree's ability to fit the training data and its size or complexity, under the assumption that simpler models generalize better to unseen data."

    explain["c difference"] = "Approach to Model Complexity"
    explain["c difference explain"] = "MDL Principle involves a trade-off between the goodness of fit of the model to the data and the complexity of the model itself, where complexity is measured in terms of the length of the description needed to encode the model. Pessimistic Error Estimate, on the other hand, directly modifies the error estimate of a decision tree by adding a penalty term that increases with the complexity of the tree (for example, the number of leaf nodes)."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x <= 0.2"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.58

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x <= 0.5")

    A = tree.insert_right("A")
    B = tree.insert_left("y <= 0.4")
    B.insert_left("A")
    B.insert_right("x <= 0.2")
    answer["c, tree"] = tree
    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.5310044

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "Handedness"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.23137821315975915
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

