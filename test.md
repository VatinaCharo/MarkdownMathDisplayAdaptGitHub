# 量子力学的数学工具

## 波函数空间

波函数空间![](https://latex.codecogs.com/png.latex?\\mathcal{F})：平方可积的充分正规函数构成的集合

### ![](https://latex.codecogs.com/png.latex?\\mathcal{F})是一个矢量空间

如果![](https://latex.codecogs.com/png.latex?\\psi_1(\\vec{r}),\\psi_1(\\vec{r})\\in\\mathcal{F})，那么![](https://latex.codecogs.com/png.latex?\\psi(\\vec{r})=\\lambda_1\\psi_1(\\vec{r})+\\lambda_2\\psi_2(\\vec{r})\\in\\mathcal{F})

关键证明步骤：

![](https://latex.codecogs.com/png.latex?\\begin{aligned}|\\psi(\\vec{r})|^2&=|\\lambda_1|^2|\\psi_1(\\vec{r})|^2+|\\lambda_2|^2|\\psi_2(\\vec{r})|^2+\\lambda_1^*\\lambda_2\\psi_1^*(\\vec{r})\\psi_2(\\vec{r})+\\lambda_1\\lambda_2^*\\psi_1(\\vec{r})\\psi_2^*(\\vec{r})\\\\&\\leqslant|\\lambda_1|^2|\\psi_1(\\vec{r})|^2+|\\lambda_2|^2|\\psi_2(\\vec{r})|^2+2|\\lambda_1||\\lambda_2||\\psi_1(\\vec{r})||\\psi_2(\\vec{r})|\\\\&\\leqslant|\\lambda_1|^2|\\psi_1(\\vec{r})|^2+|\\lambda_2|^2|\\psi_2(\\vec{r})|^2+|\\lambda_1||\\lambda_2|\\left[|\\psi_1(\\vec{r})|^2+|\\psi_2(\\vec{r})|^2\\right]\\end{aligned})

因此

![](https://latex.codecogs.com/png.latex?\\int|\\psi(\\vec{r})|\\mathrm{d}^3r=const)

### ![](https://latex.codecogs.com/png.latex?\\mathcal{F})的内积

![](https://latex.codecogs.com/png.latex?(\\phi,\\psi)=\\int\\phi^*(\\vec{r})\\psi(\\vec{r})\\mathrm{d}^3r)

**性质：**
**一对波函数的内积关于第一个因子反线性，关于第二个因子线性**
1. ![](https://latex.codecogs.com/png.latex?(\\phi,\\psi)=(\\psi,\\phi)^*)
2. ![](https://latex.codecogs.com/png.latex?(\\phi,\\lambda_1\\psi_1+\\lambda_2\\psi_2)=\\lambda_1(\\phi,\\psi_1)+\\lambda_2(\\phi,\\psi_2))
3. ![](https://latex.codecogs.com/png.latex?(\\lambda_1\\phi_1+\\lambda_2\\phi_2,\\psi)=\\lambda_1^*(\\phi_1,\\psi)+\\lambda_2^*(\\phi_2,\\psi))
4. 若![](https://latex.codecogs.com/png.latex?(\\phi,\\psi)=0)，则称![](https://latex.codecogs.com/png.latex?\\phi)与![](https://latex.codecogs.com/png.latex?\\psi)正交
5. ![](https://latex.codecogs.com/png.latex?|\\phi(\\vec{r})|=\\sqrt{(\\phi,\\phi)})
6. ![](https://latex.codecogs.com/png.latex?|(\\phi,\\psi)|\\leqslant|\\phi||\\psi|)
