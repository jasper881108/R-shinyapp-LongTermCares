


# R-shinyapp-LongTermCares
### We want to know how local Lonterm Cares sites contribute to every minimal-dministrative-area. 
### By computing some hypothesis functions considering factors below 
### 1.Distance
### 2.Capped Diminishing
### 3.Decaded utility
### Finally, We can optimize the function and find which site should keep eye on.

<br>
<br>

# Structure
### Backend             -     Django
### interactive app     -     Shiny

# Why Long-Term Cares
### This side project is prepared for 
[2021資料創新應用競賽](https://opendata-contest.tca.org.tw)

<br>
<br>
<br>
<br>

# Product demo

<br>
<br>

### Main page
![Main page](/images/Main_page.png)
![Main page2](/images/Main_page2.png)


<br>
<br>


### Acoount Page
![Login page](/images/Login_page.png)
![Register page](/images/Register_page.png)

<br>
<br>

### Video
![Product](https://user-images.githubusercontent.com/67900956/117104847-6d537480-adaf-11eb-8e79-be2ff9f374d8.mp4)
<br>
<br>
<br>
<br>

# Try it yourself
### Notice that it's doomed to be slow cause I'm paying nothing. [Long-Term Cares!!](https://goverment.shinyapps.io/shinyapp/)

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Optimize method - Using nloptr packages
### Third party pacakages to enforce non-linearaity optimize method.

<br>
<br>
<br>
<br>

![nonli_optimize method](/images/nonlinear_normal.png)
![nonli_optimize params](/images/nonlinear_logistic.png)

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Optimize method - Adam with regulization
### By simply computing gradient and adding constraint we can still perform linear optimize.

<br>
<br>
<br>
<br>

![li_optimize method](/images/linear_loss_grad.png)
![li_optimize params](/images/linear_optimizer.png)
