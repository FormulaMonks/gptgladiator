refactor_code = """Refactor the following code and explain why you did so. Think out loud.:

    const checkUserProfilesComplete = async (userIds) =>
    (
        await Promise.all(
        userIds.map((id) => getUserService('afkHd98JUcdd6LiDgC').get(id))
        )
    ).reduce(
        (acc, curr) => acc && curr.hasName() && curr.hasAge() && curr.hasPicture(),
        true
    )
"""

second = """What are the benefits and drawbacks of remote work?
"""

third = """Write a short story set in a post-apocalyptic world.
"""
