mock_responses = [
    "Here is the refactored code:\n\n```js\nconst checkUserProfilesComplete = async (userIds) => {\n  const users = await Promise.all(userIds.map((id) => getUserService('afkHd98JUcdd6LiDgC').get(id)));\n  return users.every((user) => user.hasName() && user.hasAge() && user.hasPicture());\n}\n```\n\nIn this refactored code, the `await` statement is used to wait for all the user objects to be fetched using `Promise.all()`. Then, the `every()` method is used to check if all users have `hasName()`, `hasAge()`, and `hasPicture()` properties. The `every()` method returns `true` if all elements of the array pass the callback function, hence no need for an initial value of `true` in the `reduce()` method.", 
    "Here's a refactored version of the code:\n\n```\nconst checkUserProfilesComplete = async (userIds) => {\n  const users = await Promise.all(userIds.map(id => getUserService('afkHd98JUcdd6LiDgC').get(id)));\n  return users.every(user => user.hasName() && user.hasAge() && user.hasPicture());\n}\n```\n\nChanges made:\n- Added curly braces around the function body for clarity and maintainability.\n- Stored the result of `Promise.all()` in a variable called `users`.\n- Used the `every()` method instead of `reduce()` to check if all users have completed profiles. This is more intuitive since we are checking if every user matches a certain condition.", 
    "There are not much details provided regarding the functionality of the code and requirements for refactoring. However, here are some possible refactorings you could apply:\n\nOption 1)\n\nIn this option, we store the result of `getUserService('afkHd98JUcdd6LiDgC')` in a variable and use it in the `map` method call. }"
]

mock_grades = """
[
    {      
        "score": 100,     
        "explanation": "The refactored code is accurate, concise, and uses the right methods (`Promise.all()` and `every()`). It also provides a clear explanation of how the code works."\n   
    },   
    {
        "score": 90,        
        "explanation": "This answer also provides a correct refactored code, but the changes mentioned are already present in the first response, so it has a slightly lower score than the first one."\n    
    },    
    {        
        "score": 40,
        "explanation": "This answer doesn\'t provide a refactored code but outlines a possible change that could be made. It is not as helpful as the first two responses."\n    
    }
]
"""
    