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
    level1["smoking_info_gain"] = 0.2780719051126377

    level1["cough"] = -1
    level1["cough_info_gain"] = 0.034851554559677034

    level1["radon"] = -1
    level1["radon_info_gain"] = 0.2364527976600279

    level1["weight_loss"] = -1
    level1["weight_loss_info_gain"] = 0.02904940554533142

    level2_left["smoking"] = -1
    level2_left["smoking_info_gain"] = 0

    level2_right["smoking"] = -1
    level2_right["smoking_info_gain"] = 0

    level2_left["radon"] = -1
    level2_left["radon_info_gain"] = 0

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219280948873623

    level2_left["weight_loss"] = -1
    level2_left["weight_loss_info_gain"] = -1

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219280948873623

    level2_right["cough"] = -1
    level2_right["cough_info_gain"] = -1

    level2_right["weight_loss"] = -1
    level2_right["weight_loss_info_gain"] = -1

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree() 
        
    tree = u.BinaryTree('Smoking Tobacco')

    cough = tree.insert_left('Chronic Cough')
    radon = tree.insert_left('Radon Exposure')

    cough.insert_right(1)
    cough.insert_left(4)

    radon.insert_left(1)
    radon.insert_right(4)
    answer["tree"] = tree  
    answer["training_error"] = 0.0  




    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    answer["(a) entropy_entire_data"] = 1.4253642047367425

    answer["(b) x <= 0.2"] = 0.17739286055515824
    answer["(b) x <= 0.7"] = 0.3557029418697566
    answer["(b) y <= 0.6"] = 0.34781842724338197

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y <= 0.6")
    left = tree.insert_left("x <= 0.7")
    right = tree.insert_right("x <= 0.2")

    left.insert_left("B")
    
    y_03 = left.insert_right("y <= 0.3")
    y_03.insert_left("A")
    y_03.insert_right("C")

    right.insert_right("A")
    y_08 = right.insert_left("y <= 0.8")
    y_08.insert_right("B")
    y_08.insert_left("C")

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
    answer["(f) explain choice"] = "Car type has the lowest Gini index of all, excluding ID. ID is an identification column and cannot be treated for the Gini index, as it holds no value in that context. With a lower Gini index, Car Type is a purer class than Shirt Size, and so is a better attribute to split on."
    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

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

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Continuous because each measure can be subdivided into smaller measures continuously. Quantitative because its value is held in its numerical value. Ratio because there is a 0; at midnight, the day begins and you cannot go back from it, that would be another day, hence another system of reference."

    answer["b"] = [d, qn, r]
    answer["b: explain"] = "Discrete because a human tool is always discrete, even to the finest of values. Quantitative because its value is held in its numerical value. Ratio because there is a 0; when it is completely dark out, and there is no light you cannot go back from it."

    answer["c"] = [d, qn, o]
    answer["c: explain"] = "Discrete because there are only finite ways of describing light levels. Qualitative because its value is held in a person's judgement, not a number. Ordinal because it is assumed the judgements take the form of 'Dim', 'Bright', 'Very Bright'..."

    answer["d"] = [c, qn, r]
    answer["d: explain"] = "Continuous because each measure can be subdivided into smaller measures continuously (i.e. 0.00000000000023° and so on). Quantitative because its value is held in its numerical value. Ratio because there is a 0; an angle cannot be -5° wide. "

    answer["e"] = [d, ql, o]
    answer["e: explain"] = "Discrete because there are only 3 levels. Qualitative because the value is held in a title (or better yet, a metal) and not a number. Ordinal because it describes the ordr of performance."

    answer["f"] = [c, qn, i]
    answer["f: explain"] = c_exp + qn_exp + 'Interval because a 0 is not present, you can go below sea level; the same analogy applies with the different categorization between Celsius and Kelvin.'

    answer["g"] = [d, qn, r]
    answer["g: explain"] = "Discrete because patients are measured in natural numbers." + qn_exp + r_exp + "You cannot have -1 person."

    answer["h"] = [d, ql, n]
    answer["h: explain"] = "Discrete because you cannot have a fraction of an ISBN. Qualitative because the value is held in an identifier. Nominal because there is no inherent hierarchy or other operation, aside from equality and inequality, that can be made on it."

    answer["i"] = [d, ql, o]
    answer["i: explain"] = "Discrete because there are only 3 levels. Qualitative because the value is held in a judgement. Ordinal because it describes the level of light-passing from more opaque to more translucent."

    answer["j"] = [d, ql, o]
    answer["j: explain"] = "Discrete because there is a fixed number of military ranks which cannot be subdivided. Qualitative because the value is held in a rank rather than a number. Ordinal because it describes ranks among military personnel."

    answer["k"] = [c, qn, r]
    answer["k: explain"] = c_exp + qn_exp + r_exp + "When standing right at the center, that is the 0, you can't get closer to the center whilst also being there."

    answer["l"] = [c, qn, r]
    answer["l: explain"] = c_exp + qn_exp + r_exp + "0 Density is a theoretical value, however I am not sure if it possible. The 0 is present."

    answer["m"] = [d, ql, n]
    answer["m: explain"] = "Discrete because you cannot subdivide a coat check number. Qualitative because the value is held in the identifier. Nominal because it is an identifier, there is no comparison or other operations, other than equality or inequality, to be made."

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

