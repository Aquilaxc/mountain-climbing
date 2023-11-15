# Track4：爬楼梯

## 一、作品介绍

### 1. 作品标题

**爬楼梯**

### 2. 作品特点

通过矩阵对称性进行矩阵快速幂优化，显著提高运算速度。

### 3. 设计思路

#### 3.1 问题转化
由描述可知，爬楼梯的问题本质上是一个斐波那契数列。因此，将本问题转化为求解

上第1级台阶有1种方法，上第2级台阶有2种方法，而斐波那契数列的前n项为1， 1， 2， 3……。
因此，第1024级台阶实际上为斐波那契数列第1025项。问题的关键在于求解斐波那契数列的第1025项。

#### 3.2 矩阵表示

斐波那契数列可以用矩阵表示递推关系：

$$
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
$$

#### 3.3 矩阵的幂运算

从递推公式中可以推导出，斐波那契数列本质上是求矩阵R：

$$
    R =
    \begin{bmatrix}
        a & b \\
        b & a-b
    \end{bmatrix}
$$

矩阵R中，

$$
    f_{n+1} = f_n + f_{n-1}
$$

因此矩阵R又可以简化为

$$
    R =
    \begin{bmatrix}
    a & b \\\\\
    b & a-b
    \end{bmatrix}
$$

因此，只需求出矩阵R的第1列即可。

这里使用二分法加速矩阵幂运算：

$$
    R = 
    \begin{cases}
        A^{p} \cdot A^{p}, & n=2p \\
        A^{p} \cdot A^{p}, & n=2p+1
    \end{cases}
$$

其中，

$$
    A =
    \begin{bmatrix}
        1 & 1 \\
        1 & 0
    \end{bmatrix}
$$

#### 3.4 递推公式

推导出递推公式：

$$
    a_n = 
    \begin{cases}
        a_p^2 + b_p^2, & n=2p \\
        a_p^2 + 2a_pb_p, & n=2p+1
    \end{cases}
$$

$$
    b_n = 
    \begin{cases}
        2a_pb_p - b_p^2, & n=2p \\
        a_p^2 + b_p^2, & n=2p+1
    \end{cases}
$$

#### 3.5 二进制转换

将1024转换为二进制，从最左侧第二位开始，如果是1则使用n=2p+1对应的公式，如果是0则使用n=2p对应的公式。

### 4. 运行方式

**运行环境: Python 3+**

```shell
python main.py
爬到1024级台阶的方法数=7291993184377412737043195648396979558721167948342308637716205818587400148912186579874409368754354848994831816250311893410648104792440789475340471377366852420526027975140687031196633477605718294523235826853392138525
