<script type="text/javascript"
  async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Track4：爬楼梯

# ✨ 一、作品介绍
## 1、作品标题

爬楼梯

## 2、作品特点

根据矩阵对称性进行矩阵快速幂优化，极大提高运算速度

## 3、设计思路

由描述可知，爬楼梯的问题本质上是一个斐波那契数列。因此，将本问题转化为求解斐波那契数列第n项。

上第1级台阶有1种方法，上第2级台阶有2种方法，而斐波那契数列的前n项为1， 1， 2， 3……。
因此，第1024级台阶实际上为斐波那契数列第1025项。

斐波那契数列的递推公式可以由矩阵表示为：
![image](https://raw.githubusercontent.com//Aquilaxc/mountain-climbing/tree/main/imgs/formula2.png)

<pre>
\[
\begin{bmatrix}
f_{n+1} \\
f_{n}
\end{bmatrix}
=
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
\cdot
\begin{bmatrix}
f_n \\
f_{n-1}
\end{bmatrix}
\]
</pre>


$$
\begin{Bmatrix}
    1 & 2 & 3 \\\\
    4 & 5 & 6 \\\\
    7 & 8 & 9
\end{Bmatrix} \tag{2}
$$

从递推公式中可以推导出，斐波那契数列本质上是求矩阵R：
![image](https://github.com/Aquilaxc/mountain-climbing/tree/main/imgs/formula1.png)

矩阵R中，f_{n+1} = f_n + f_{n-1}，因此矩阵R又可以简化为
![image](https://github.com/Aquilaxc/mountain-climbing/tree/main/imgs/formula3.png)

因此，只需求出矩阵R的第1列即可。

使用二分法加速矩阵幂运算，即：
![image](https://github.com/Aquilaxc/mountain-climbing/tree/main/imgs/formula4.png)

可推导出：
![image](https://github.com/Aquilaxc/mountain-climbing/tree/main/imgs/formula5.png)

将1024转换为二进制，并从最左侧第二位开始，如果是1则代表使用n=2p+1对应的公式，如果是0则代表使用n=2p对应的公式，代入公式即可算出。

由于本方法计算出的数字为第n+1项，因此可直接代入1024。


##  4、运行方式
###### 运行环境 python 3+

```shell
python main.py
爬到1024级台阶的方法数=7291993184377412737043195648396979558721167948342308637716205818587400148912186579874409368754354848994831816250311893410648104792440789475340471377366852420526027975140687031196633477605718294523235826853392138525
```

<script type="text/javascript"
  async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>