mock_responses = [
    "Here is the refactored code:\n\n```js\nconst checkUserProfilesComplete = async (userIds) => {\n  const users = await Promise.all(userIds.map((id) => getUserService('afkHd98JUcdd6LiDgC').get(id)));\n  return users.every((user) => user.hasName() && user.hasAge() && user.hasPicture());\n}\n```\n\nIn this refactored code, the `await` statement is used to wait for all the user objects to be fetched using `Promise.all()`. Then, the `every()` method is used to check if all users have `hasName()`, `hasAge()`, and `hasPicture()` properties. The `every()` method returns `true` if all elements of the array pass the callback function, hence no need for an initial value of `true` in the `reduce()` method.",
    "Here's a refactored version of the code:\n\n```\nconst checkUserProfilesComplete = async (userIds) => {\n  const users = await Promise.all(userIds.map(id => getUserService('afkHd98JUcdd6LiDgC').get(id)));\n  return users.every(user => user.hasName() && user.hasAge() && user.hasPicture());\n}\n```\n\nChanges made:\n- Added curly braces around the function body for clarity and maintainability.\n- Stored the result of `Promise.all()` in a variable called `users`.\n- Used the `every()` method instead of `reduce()` to check if all users have completed profiles. This is more intuitive since we are checking if every user matches a certain condition.",
    "There are not much details provided regarding the functionality of the code and requirements for refactoring. However, here are some possible refactorings you could apply:\n\nOption 1)\n\nIn this option, we store the result of `getUserService('afkHd98JUcdd6LiDgC')` in a variable and use it in the `map` method call. }"
]

mock_grades = """
{
    "1": {
        "score": 95,
        "explanation": "This response provided a comprehensive and clear refactoring of the code with proper explanations for each change. It improved code readability and maintainability, organizing the code in a better way. It accurately fulfilled the request."
    },
    "2": {
        "score": 85,
        "explanation": "This response provided a proper refactoring of the code, with improvements like extracting the user service and renaming the function. It also added comments to explain the code. However, it was less comprehensive than the first one and didn't mention using every() method instead of reduce()."
    },
    "3": {
        "score": 80,
        "explanation": "This response provided a good refactoring, with clear improvements such as renaming the function and using every() method. However, it was not as comprehensive as the first one, and provided fewer improvements than the second one, reconsidering extracting service id for increased reusability."
    }
}
"""
