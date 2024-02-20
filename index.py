import streamlit as st
import functions
todos = functions.get_todos()
def update_todo():
    newtodo= st.session_state["todotask"]+"\n"
    todos.append(newtodo)
    functions.write_todos(todos)

st.title('Todo Diary - Girija')
st.subheader("Demo App")
st.write("This app maintains the task")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._experimental_rerun()

st.text_input(label='',placeholder='Enter a new Todo Task here...', on_change=update_todo,key='todotask')


