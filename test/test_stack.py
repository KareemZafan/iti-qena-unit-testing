from src.stack import Stack
import pytest

class TestStack:
    
    @pytest.mark.FEB
    def test_push(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        my_stack.push(5)
        my_stack.push(90)

        assert my_stack.get_size() == 6
        assert my_stack.get_peek() == 90
        assert my_stack.get_current_stack() == [1,2,3,4,5,90]

    @pytest.mark.FEB 
    def test_pop(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        popped_item = my_stack.pop()
        assert popped_item == 3 
        assert my_stack.get_peek() == 2
        my_stack.push(4)
        my_stack.push(5)
        my_stack.push(90)

        assert my_stack.get_size() == 5
        assert my_stack.get_peek() == 90
        assert my_stack.get_current_stack() == [1,2,4,5,90]  

