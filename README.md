---
title: "R shinyapp LongTermCares"
output: html_document
---

<style>
body {
    position: absolute;
    left: 0px;}
</style>
<br>


#### Optimizer

####  Loss function to optimize

<br>
$$Loss \:\: = \:\: \sum_{n=1}^{i}\frac{ \lambda \cdot (\: \frac{d_i}{100}^{-\alpha} \cdot r_i \: )^{\beta}\:}{n_c}  + \:  reg \: \cdot \: \left\lvert\: \sum_{n=1}^{i}( r_i-10 )\: \right\rvert \:\:\:\:\: (\:for \: n_c >0 \:) $$
<br>

####  Analystic gradient of  $r_i$

<br>
$$ \frac{\partial L}{\partial r_i} \:\: = \:\: \sum_{n=1}^{i} \frac{\lambda \cdot \beta \cdot (\: \frac{d_i^{-\alpha}}{100} \cdot r_i \: )^{\alpha\beta} \cdot r_i^{\beta-1} }{n_c} + \:  reg \: \cdot \sum_{n=1}^{i}\: \frac{(r_i-10)}{\left\lvert r_i-10  \right\rvert} \:\:\:\:\: (\:for \: n_c >0 \:) $$
<br>

+ $lr :  learning\:\: rate \:\:of \:\:10$<br>
+ $beta1 : exponential \:\: moving \:\:average \:\:of \:\:\:Mean \:\:\: is \:\: 0.99$<br>
+ $beta2 : exponential \:\: moving \:\:average\:\:of \:\: \:Variance \:\:\: is \:\: 0.999$<br>
+ $reg : regulization \:\:strength \:\:defined \:\:by \:\:initial\:\:loss$<br>
+ $N : number \:\: of  \:\:cells \:\: in \:\:town$
+ $R : resource \:\:units$
+ $D : distance \:\:matrix \:\: N \:\:by \:\: R$
+ $n_c :  number\:\: of \:\:demand \:\: in\:\: cells$<br>
+ $d_i : i_{th} \:\: column \:\:of \:\: D$<br>
+ $r_i : i_{th} \:\:units \:\:of \:\:R$<br>
