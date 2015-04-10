
#INFO290: Data Mining & Analytics
##April 2nd- Spectral Clustering Lab/Homework

This assignment requires you to do spectral clustering in MATLAB. Since you will need to look at plots in MATLAB, you will need to access the MATLAB GUI. If you don’t already have MATLAB on machine, your options for getting access to MATLAB are:
connect to info290t@dlab-matlab.berkeley.edu using X-Windows over SSH
instructions for different operating systems are here: https://docs.google.com/document/d/1nwAoNbvoTYw0yEdgPQzX6jbe4PB24Mes6DeReVQcMnI/edit
credentials to dlab-matlab server: username info290t, password: ****
Request to download MATLAB from UC Berkeley (it’s now free for students). Fill out the student form here (make sure you are logged into your @berkeley.edu account).
Note: it may take some time for your request to be approved.


**Description:** In this lab you will gain basic familiarity with how to run the spectral clusterings methods demonstrated in class on Tuesday. 

**Dataset:** You will be following directions to create your own synthetic datasets consisting of radial distributions of data points. 

**Accuracy measure:** For one of the questions we’ll be using the “Hungarian” method, in order to calculate the correspondence between the cluster assignments and the true generating distributions. The file “accuracy.m” in the zip file will be used to calculate this.

**Deliverables:** Please submit to bCourses 1) a PDF with your answers and write up for questions 3-8 (8 is bonus).

This Lab is due at 10am next Thursday and will count as a homework. Grading will be based on completion of questions 1-7 and the thoroughness of experimentation.  MAX GROUP SIZE: 4

How to quickly get started (skip to question 1 for the longer version):
unzip spectralclustering-1.1.zipcd spectralclustering-1.1
matlab
load X
runexpl2(X,2,8)


###Questions/Objectives
1. Get started with the spectral clustering package in MATLAB
  1.Unzip spectralclustering-1.1.zip into any directory. This will create a directory called “spectralclustering-1.1”
  2.Launch matlab
  3.Within MATLAB, change to within the directory that was unzipped in step a). The change directory command in matlab is the same as in Linux or any OS.
  4.Type ‘ls’ to see the contents of the directory. Any files with “.m” suffix are matlab functions. You can run any of those function by simply typing the filename without the suffix. 
2. Load a sample dataset and run spectral clustering with default parameters
  1. A two dimensional (two features) dataset is available in the file “X.mat”, which stores a matrix called “X.” To load this saved matrix into the matlab environment, type “load X.”
  2. Now, generate a similarity matrix by typing A=gen_nnd(X, 7, 500); This returns a similarity matrix ‘A’ and specifies that the similarity matrix should use the ‘7’ nearest neighbors and a block size of 500. Block size specifies the number of instances (rows) that should be processed at a time. 
    NOTE: there was a typo where gen_nnd was called with “A” instead of “X”
  3. Next, feed the similarity matrix to the spectral method which will create a Laplacian, perform eigen decomposition, and return the cluster assignments based on k-means being run on the top k eigen vectors. The command for running this is: [clusters, evals] = sc(A, 0, 2). This function “sc” returns two data objects (both vectors); the cluster assignments, and the eigen values. The “[clusters, evals] notation simply saves the two outputs to variables of those names. The “sc” function takes as input a) the similarity matrix “A” b) the sigma setting (a value of 0 tells it to auto tune this value), and c) specification of the number of clusters. 
3. Visualize the results in a scatter plot
  1. Now that we have cluster assignments to every row of our X matrix, let’s now visualize the data points in X and color the points according to their spectral clustering assignments. To do this, type scatter(X(:,1), X(:,2), 5, clusters). This command’s inputs are a) the original 2-dimensional matrix, the “font” size of the points in the plot, and an array that contains a “color grouping.” A color grouping is simply an integer assignment that will be mapped to a color based on the default scatter plot color scheme. Our “clusters” array from the spectral clustering output will serve as the color grouping. 
  2. Save this image to your report
4. Did spectral clustering properly cluster the two radial distributions of data points? 
  1. Often (but not guaranteed) the eigen values will tell us how good of a clustering we have achieved. When the values are all ‘1’ there is a better chance that we’ve achieved an optimal clustering. What were the eigen values?
5. The user tunable parameters for spectral clustering are setting the nearest neighbor number and K. The rule of thumb for nearest neighbor is the ceiling of the log of the number of data points. Try values for k-nn that range from -5 to +5 of that rule of thumb. The -5 to 5 is ceil(log(size(X,1)))-5 to ceil(log(size(X,1)))+5 for the knn value. 
  1. Which nearest neighbor number gives you the best clustering? 
6. Generate your own dataset
  1. The dataset loaded in from the X.mat file contained data points generated from two radial distributions. The function “randr” creates data points generated from a  distribution with radius R, data points N, and variance V and returns N pairs of X and Y values. For example, [x,y] = randr(10, 1000, 0.05) will return x and y vectors based on a radial distribution with radius 10 and variance 0.05. 
  2. In order to create a dataset that consists of two different distributions, like the X.mat dataset, you’ll use randr twice to create two pairs of vectors and then combine them. For example, the following commands would create an alternative to the X dataset, called X2
            ```[x1,y1] = randr(50, 5000, 0.10);
            [x2,y2] = randr(20, 4000, 0.05);
            x = [x1 x2]’;
            y = [y1 y2]’;
            X2 = [x y];
            scatter(x,y);```
  4. Create your own two distribution dataset, experimenting with different values for variance, radius, and data points.
7. Use the runexpl2 command to run spectral clustering on your own dataset. The runexpl2 command executes the same commands you executed in steps 1-3. It returns a vector of spectral cluster assignments and takes as input the original matrix, the number of clusters, and the number of nearest neighbors and then visualizes the clustering. Tune the nearest neighbor parameter to find a good fitting clustering. If the nearest neighbor settings still doesn’t result in good clusterings, try reverting to the manual steps of 1-3 and modify the sigma value (not auto tune). 
  1. Repeat this processes for three different datasets you create on your own
    1. One of the three must be a three distribution dataset
    3. Save images of the scatter plots to your report 
    3. Explain your processes of attempting to achieve a good clustering for each of the datasets
    4. use the accuracy function to report the accuracy of the best clustering for each of the three datasets. The accuracy function takes in to arguments, the first is the array of spectral cluster assignments, the second is the array of ground truth assignments. The ground truth assignments for the example dataset in 6b would be: [ones(5000,1);2*ones(4000,1)];
8. Bonus question (+ 40% credit)
  1. The paper that was assigned for class today showed how two different clusters could be identified even when their data points overlapped one another if one of the distributions had a tighter density than the other. Can you generate a two distribution dataset that overlaps one another and successfully distinguish between the two?
  2. For example, randr(100, 10000, 0.05) and randr(85, 10000, 0.40) overlap one another. The tuning used in the code sc.m is slightly different than the one described in the paper. Modification of the code may be necessary to achieve a solution.

## Answers
4. The spectral clustering did not produce perfect clusters. The two eigen values are 1.0 and .9998.
5. 9 gives us the perfect clustering with the eigen values at 1.0 and 1.0.
