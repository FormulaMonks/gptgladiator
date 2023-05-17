def drafts_template(i, response, max_line_height):
    return f"<div class='draft' style='height:{max_line_height}px;'><div><b>Draft {i + 1}</b></div><div><pre><code class='language-python'>{response['content']}</code></pre></div></div>"


def grades_template(score, explanation, is_winner):
    class_name = "winner" if is_winner else ""
    return f"<div class='{class_name} score'><div><b>Score {score}</b></div>{explanation}</div>"


stylesheet = """
<style>
.draft {
    padding: 10px;
    border: 1px solid #ccc; 
    border-radius: 8px; 
    background-color: #f2f2f2; 
    margin: 5px;
}
.score {
    padding: 10px;
    border: 1px solid #ccffff; 
    border-radius: 8px; 
    background-color: #e6ffff; 
    margin: 5px;
}
.winner {
    border: 3px solid #33cc33; 
}
</style>
"""
