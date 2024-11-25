import streamlit as st
import datetime 


st.set_page_config(page_title="Mj's Biography", page_icon="🤡", layout="centered")

if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False

def Drawing_button():
    st.session_state.toggle_state = not st.session_state.toggle_state
    
    
    
    
st.markdown(
    """
    <div style="text-align: center; font-size: 40px;">
        <strong>😲 MJ's BIOGRAPHY 😲</strong>  
    </div>
    """,
    unsafe_allow_html=True,
)

    
    
    
with st.container(): 
     st.write("---") 
     left_column, right_column = st.columns(2) 
     with left_column:
        

        
        
        st.write("")
        st.write("")
        
        st.image('profilepicture.jpg', use_container_width=True)
        st.text_input("My Name", "Marlon jr. E. Cabahug")
        st.write("---") 
        
        
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>What I do</strong>
            </div>
        """, unsafe_allow_html=True)
         
        
        
        st.text_area("","""- I draw 
- I sleep
- I ride bicycle
- I watch movies from pirated sites""", height=125 )
        st.write("---")
        
        st.markdown("""
            <div style="text-align: center; font-size: 23px;">
               <strong>Click to see all the pictures of my hobbies and achievements</strong>
            </div>
        """, unsafe_allow_html=True)
        st.write("   ")
        st.write("   ")
        st.write("   ")
        
        col1, col2, col3 = st.columns(3)

       
        with col1:
            st.write('')

        with col2:
            if st.button("click here"):
                Drawing_button()

        with col3:
            st.write('')
            
        
        if st.session_state.toggle_state == True:
            st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>My drawings</strong>
            </div>
            """, unsafe_allow_html=True)
            st.write("---")
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.image('drawing 1.jpg', width=150)
                st.image('drawing5.jpg', width=150)
            
                st.image('drawing 3.jpg', width=150)
                st.image('drawing7.jpg', width=150)

            with inner_col2:
                st.image('drawing2.jpg', width=150)
                st.image('drawing4.jpg', width=150)
                st.image('drawing6.jpg', width=150)
                st.image('drawing8.jpg', width=150)
            st.write("---")   
            
            
            st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Accomplishment</strong>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.image('reseach1.jpg','We got second place in innovation category in best research', width=150)
            with inner_col2:
                st.image('reseach2.jpg','this is our reseach, this is basically sucks up oil in the ocean', width=150)
            
            st.write("---")
            
            
            st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>My cycling hobby</strong>
            </div>
            """, unsafe_allow_html=True)
            st.write("---")            
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.image('bike1.jpg','this is when I got my new bike', width=150)
            with inner_col2:
                st.image('bike2.jpg','HELL YEAHH!!', width=150)
            
            st.write("---")   
            
            st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Bonus ✨</strong>
            </div>
            """, unsafe_allow_html=True)
            st.write("---")            
            
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.image('mypet (1).jpg','Wanda', width=150)
                st.image('mydog (2).jpg','Shaque', width=150)
                
            with inner_col2:
                st.image('mypet (3).jpg','Panda', width=150)
                st.image('mypet (2).jpg','tisay', width=150)
      
        st.write("---")  
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Social Media Accounts</strong>
            </div>
        """, unsafe_allow_html=True)
        
        
        
        
        col1, col2, col3 = st.columns(3)
            
        with col1:
            st.write('')

        with col2:
            st.write("[Facebook](https://www.facebook.com/profile.php?id=100090975026071)")
            st.write("[Instagram](https://www.instagram.com/mjay.cabahug/?igsh=NWVnMmNiOWg3MTBx&fbclid=IwY2xjawGv2dVleHRuA2FlbQIxMAABHRyufPcsJO5y5NMdKJqTXz9K82xrwQKedo1uJnRQbz94zBAZQPNv_r1UtQ_aem_wZg6nnp58nuCFK6NA74R7Q)")         
         

        with col3:
            st.write('')   
            
            
            
            
     with right_column:
        
        
        
        st.text_area("", """Hi, I’m Marlon Jr. E. Cabahug!, MJ for short, it's an abbreviation of Marlon and Jr. I’m someone who loves drawing, watching anime and movies sleeping, and riding my bicycle during my downtime. Each of these hobbies brings a unique sense of joy and relaxation to my life. Whether it's creating something artistic or simply exploring the outdoors, I find happiness in both creativity and simplicity.    """, height = 200)
        age = st.selectbox("Age", [str(i) for i in range(18, 101)])
        
        mbday = st.date_input(" Birthday", datetime.date(2006, 8, 6))
    
        st.text_input("place of birth", "Surigao City, Surigao del Norte")
        st.radio("Gender", ["Male", "Female"])
        
        st.write("---")
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Educational Attainment</strong>
            </div>
        """, unsafe_allow_html=True)
        
        hs = st.text_input("High School", "Surigao City National Highschool")
        shs = st.text_input("Senior High School", "Surigao del Norte National highschool")
        college = st.text_input("College", "Surigao del Norte State University")
        st.write("---")
        
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>family background</strong>
            </div>
        """, unsafe_allow_html=True) 
        mother = st.text_input("Mother's name", "Ma. Elena G. Ensomo")
        
        mbday = st.date_input("Mother's Birthday", datetime.date(1970, 1, 7))
     
        father = st.text_input("Father's Name", "Marlon L. Cabahug")
        mbday = st.date_input("Father's Birthday", datetime.date(1969, 6, 30)) 
      
        st.text_input("My big sister's Name", "Princess Pychine E. Cabahug")
        mbday = st.date_input("My big sister's Birthxday", datetime.date(2004, 10, 9))
        
