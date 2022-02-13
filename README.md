# SaaS
HashCode 2K21

## Theme: Responsible AI
Learning models are famously as biased as their training data and developers need to be careful about what data they use and how it is represented in their training and testing sets.
<br>This project aims to use certain corrective measures to mitigate such latent biases.

## Proposed Solution
Our solution will involve the use of debiasing-Variational Autoencoders (DB-VAE) first proposed by Alexander Amini et al in 2019. This algorithm will help identify under-represented examples and increase the probability at which the learning algorithm samples these data points. The latent variables that cause these biases are learnt by the DB-VAE during training and must effectively reduce errors.

## References
> [Examples of bias in ML Models from the Guardian](https://www.theguardian.com/inequality/2017/aug/08/rise-of-the-racist-robots-how-ai-is-learning-all-our-worst-impulses)
> 
>[Variational Auto-Encoders  	arXiv:1312.6114](https://arxiv.org/abs/1312.6114)
>
>[Uncovering and Mitigating Algorithmic Bias through Learned Latent Structure - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Debiasing-Variational-Autoencoder-Architecture-of-the-semi-supervised-DB-VAE-for-binary_fig2_334381622 [accessed 12 Feb, 2022]<br>
>
><a href="https://www.researchgate.net/figure/Debiasing-Variational-Autoencoder-Architecture-of-the-semi-supervised-DB-VAE-for-binary_fig2_334381622"><img src="https://www.researchgate.net/profile/Ava-Soleimany/publication/334381622/figure/fig2/AS:779301393813504@1562811339841/Debiasing-Variational-Autoencoder-Architecture-of-the-semi-supervised-DB-VAE-for-binary.png" alt="Debiasing Variational Autoencoder. Architecture of the semi-supervised DB-VAE for binary classification (blue region). The unsupervised latent variables are used to adaptively resample the dataset while training."/></a>
>
> © MIT 6.S191: Introduction to Deep Learning
>
> http://introtodeeplearning.com


