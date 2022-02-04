########################################################

#Copyright (c) DeepSphere.AI 2021

# All rights reserved

# We are sharing this partial code for learning and research, and the idea behind us sharing the source code is to stimulate ideas #and thoughts for the learners to develop their MLOps.

# Author: # DeepSphere.AI | deepsphere.ai | dsschoolofai.com | info@deepsphere.ai

# Release: Initial release

#######################################################


import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from content_create import main



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        







def mainfn():
#     local_css("style1.css")
#     col1, col2, col3 = st.beta_columns(3)
#     image1 = Image.open('aws.png').convert('RGB')
#     image2 = Image.open('sap.png').convert('RGB')
#     image3 = Image.open('gcp.png').convert('RGB')
    
#     st.image(image)
    # st.title('World\'s Number One Personalized Learning Management Platform')
    st.markdown('<h2>World\'s Number One Personalized Learning Management Platform</h2>',unsafe_allow_html=True)
    st.markdown('<hr style="border-top: 6px solid #8c8b8b; width: 150%;margin-left:-180px">',unsafe_allow_html=True)
#     wc_col1,wc_col2,wc_col3 = st.beta_columns((1,1,1))
#     wc_col1.image(image1)
#     wc_col2.image(image2)
#     wc_col3.image(image3)
    # bootstrap 4 collapse example
    components.html(
        """
        <!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Fonts -->
    <!-- Bootstrap CSS -->
    <!-- <link rel="stylesheet" href="css/bootstrap.min.css"> -->
<!-- <script src="js/bootstrap.min.js"></script> -->
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>

<!-- Latest compiled and minified JavaScript -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<style>
.prt1 {
    background: #0062cc;
}
.prt2 {
    background: #28a745;
    display: flex;
    align-items: center;
    justify-content: center;
}
.prt2 h2 {
    font-size: 40px;
    color: #fff;
	font-family:Conv_aqrswfte;
}
.prt2 h2 span{
	color:orange;
}
.prt3 {
    border-left: 10px solid #eee;
}
.prt3 {
    border-left: 10px solid #eee;
    padding: 0px !important;
}
.sec-part1 h1{
	font-size: 40px;
    color: #000;
	display: flex;
    align-items: center;
    justify-content: center;
	font-family:Conv_aqrswfte;
}
.thir-part1 {
   background: #0062cc;
}
img {
    width: 100%;
    max-width: 100%;
}
.thir-part2 {
    background: white;
}
.thir-part2 {
    padding: 45px 0px;
}
.fourth-part1 {
    # background: white;
    # padding: 5px 0px;
    # position: absolute;
    # bottom: 50px;
    # left: 0;
}
iframe {
    height: 430px !important;
}
.cont-part {
    width: 50%;
    float: left;
}
.txt-box1 {
  width: 280px;
    position: relative;
    padding: 25px 0px;
    height: 296px;
    line-height: 1.8;
}
.txt-box1 h4 {
    border-bottom: 2px solid #fff;
    display: block;
	font-size: 25px;
    font-family: Conv_aqrswfte;
	text-align: center;
    padding: 10px 0px;
	color:#fff;
}
.txt-box1.wnt-cnt {
    background: #191970;
    border: 1px solid #191970;
}
.txt-box1.wnt-que{
  background: #9ACD32;
    border: 1px solid #9ACD32;
}
ul.txt-ul li{
    color: #fff;
}
.sec-part3 {
    display: flex;
    align-items: center;
    justify-content: center;
}
.thir-part2.loginbody .row {
    margin: 0px;
}
span.started-crse {
    display: block;
    position: absolute;
    bottom: 2px;
    left: 30%;
    right: 30%;
    text-align: center;
}
span.started-crse a {
    color: #fff;
    font-size: 12px;
	cursor: pointer;
}
ul.txt-ul {
    margin: 5px 0px;
}
.thir-part1 {
    display: flex;
    align-items: center;
    justify-content: center;
}
.thir-part1 h3 {
    color: orange;
    font-size: 18px;
    padding: 0px 30px;
    line-height: 1.5;
}
.txt-box1.wnt-que ul li {
    color: #000;
}
.third-part{
    padding-bottom: 10px;
    padding-left: 50px;
}
</style>
</head>
<body>


  
  <div class="container-fluid">
<div class="first-part">
   <!-- <div class="row justify-content-end">
       <div class="col-sm-6 col-md-3 prt1"></div> 
      <div class="col-sm-6 col-md-6 prt2"><h2>Deepsphere.<span>AI</span> Reinvents Education</h2></div>
	  <div class="col-sm-3 col-md-3 prt3"><img src="images/logopar.png"></div>
    </div>-->
</div>
<div class="second-part">
    <div class="row">
      <div class="col-sm-12 col-md-12 sec-part1">
		  <!--<div class="row justify-content-md-center">
			   <div class="col-md-3 col-sm-3 sec-part2">
				<img src="images/deeplogo.png">
			  </div> 
			  <div class="col-md-9 col-sm-9 sec-part2">
				<h1>World's Number One Personalized Learning Management Platform</h1>
			  </div>-->
		  </div>
	  </div>
    </div>
</div>
<div class="third-part">
    <div class="row justify-content-md-center">
			<div class="col-sm-12 col-md-12 thir-part2 loginbody"> 
				<div class="row justify-content-md-center">
				<div class="col-md-3">		
			</div>
					<div class="col-md-3 cont-part">
						<div class="txt-box1 wnt-cnt">
							<h4>I Want Content</h4>
							<ul class="txt-ul">
								<li>Faculty Assistant</li>
								<li>Student Assistant</li>
								<li>Study Material</li>
								<li>Learning Resources</li>
								<li>Lab Material</li>
							</ul>
							<!--<span class="started-crse"><a href="javascript:void();">Get Started >></a></span>-->
						</div>
					</div>
					<div class="col-md-3 cont-part">
						<div class="txt-box1 wnt-que">
							<h4>I Want Question</h4>
							<ul class="txt-ul">
								<li>Assessment</li>
								<li>Assignment</li>
								<li>Quizes</li>
								<li>Multiple Choice</li>
								<li>Fill in the blanks</li>
								<li>True or False</li>
								<li>Match the Following</li>
							</ul>
							<!--<span class="started-crse"><a href="javascript:void();">Get Started >></a></span>-->
						</div>
					</div>
				</div>
			</div>
    </div>
</div>
<div class="footer">
<div class="row">
      <div class="col-sm-12 col-md-12 fourth-part1">
		 <div class="footer-copyright  copyryt text-center">© 2021 <a href="https://www.deepsphere.ai/">DeepSphere.ai.</a> All rights reserved</div>
	  </div>
 </div>
</div>
    
  </div>


</body>
</html>



        """,
        height=600,
    )    
    
    return st
    
    
    
    
    
    
if __name__=='__main__':
    mainfn()
#     side_1, side_2 = st.beta_columns(2)
#     if side_1.button('Explore Content'):
#         st.write('B1')
#     if side_2.button('Explore Question'):
#         st.write('B2')
        
#     if st.button("button1"):
#         pass
#     if st.button("button2"):
#         pass
#     x = st.button(st.image(img))
#     st.write("Button Clicked!")
#     if st.button('button1'):
#         pass
#     if st.button('button2'):
#         pass
    