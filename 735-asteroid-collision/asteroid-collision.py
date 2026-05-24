class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids:
           
            while st and ast < 0 and st[-1] > 0:
                if abs(ast) > st[-1]:
                    st.pop()       
                    continue
                elif abs(ast) == st[-1]:
                    st.pop()       
                break              
            else:
                
                st.append(ast)

        return st
        
        