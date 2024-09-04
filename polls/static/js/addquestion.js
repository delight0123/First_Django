function updateChoiceType() {
    const voteType = document.getElementById('id_vote_type').value;
    const choiceContainer = document.getElementById('choice-container');
    if (voteType === 'single') {
        choiceContainer.innerHTML = `
            <label for="id_choice_text">选项</label>
            <input type="radio" name="choice" id="id_choice_text" required>
            <input type="text" name="choice_text" id="id_choice_text" required>
        `;
    } else if (voteType === 'multiple') {
        choiceContainer.innerHTML = `
            <label for="id_choice_text">选项</label>
            <input type="checkbox" name="choice" id="id_choice_text" required>
            <input type="text" name="choice_text" id="id_choice_text" required>
        `;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('id_vote_type').addEventListener('change', updateChoiceType);
    updateChoiceType();  // 初始化时调用一次
});