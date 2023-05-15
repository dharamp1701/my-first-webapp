import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo= st.session_state['new_todo']+'\n'
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo APP")
st.header("THIS IS my todo app")
st.subheader("welcome to new journey")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label =' ',placeholder='add new todo in todos list',
              on_change=add_todo,key='new_todo')

st.session_state
print("hello")