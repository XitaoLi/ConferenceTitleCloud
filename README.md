<!-- README English -->
# Conference Title Cloud

[中文](README_CN.md)

A tiny tool designed to visualize word clouds based on the title of the NLP conference for a particular year.
## Why Use Wordcloud
Taxonomy of conference papers is challenge now. Due to the explosive growth in accepted NLP papers, it's more and more hard to explore the work of top researchers. Inspired by Yang Chen [[1](https://zhuanlan.zhihu.com/p/577523149)], the wordcloud based on titles provides an intuitive understanding of the current state of the field. That's why this project may be helpful. 

Supported conferences:
- ACL
- EMNLP
- to be updated if necessary
## How to Run
1. Prepared for the packages.
    
    `pip install -r requirements.txt`
2. Run the project

    ```bash
    python main.py 
    options:
        --conference CONFERENCE, -c CONFERENCE
        -y YEAR, --year YEAR
        --track {finding,main,null}
        --all

    #Iterate over
    python main.py --all

    or

    python main.py -c ACL -y 2020
    ```
## Results
### ACL
<table>
  <tr>
    <td align="center">
      <img src="figs/ACL_2023_main.png"  width="400" height="200">
      <br>ACL 2023 Main
    </td>
    <td align="center">
      <img src="figs/ACL_2023_finding.png" width="400" height="200">
      <br>ACL 2023 Finding
    </td>
    <!-- 添加其他图像 -->
  </tr>
  <tr>
    <td align="center">
      <img src="figs/ACL_2021.png" width="400" height="200">
      <br>ACL 2021
    </td>
    <td align="center">
      <img src="figs/ACL_2020.png"  width="400" height="200">
      <br>ACL 2020
    </td>
    <!-- 添加其他图像 -->
  </tr>
  <tr>
    <td align="center">
      <img src="figs/ACL_2019.png" width="400" height="200">
      <br>ACL 2019
    </td>
  </tr>
</table>

### EMNLP
<table>
  <tr>
    <td align="center">
      <img src="figs/EMNLP_2022.png"  width="400" height="200">
      <br>EMNLP 2022
    </td>
    <td align="center">
      <img src="figs/EMNLP_2021.png" width="400" height="200">
      <br>EMNLP 2021
    </td>
    <!-- 添加其他图像 -->
  </tr>
  <tr>
    <td align="center">
      <img src="figs/EMNLP_2020.png" width="400" height="200">
      <br>EMNLP 2020
    </td>
    <td align="center">
      <img src="figs/EMNLP_2019.png"  width="400" height="200">
      <br>EMNLP 2019
    </td>
    <!-- 添加其他图像 -->
  </tr>
  <tr>
    <td align="center">
      <img src="figs/ACL_2019.png" width="400" height="200">
      <br>ACL 2019
    </td>
  </tr>
</table>

There are some short observations:
1. "Generation" and "Learning" consistently appear prominently across the years. 
2. In early years "attention" and "representation" attract high attention. (BTW, "xxx is all your need" is still hot today.)
3. QA, dialogue and translation are hot these years.

# Future work
LLM-based categorize and analysis for paper themes.

Contact me if you are interested in the following work.