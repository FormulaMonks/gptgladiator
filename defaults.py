default_question = """refactor the following code:

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




