document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#submit-answer').forEach(answerButton => {
        answerButton.addEventListener('click', (e) => add_answer(e));
    });
});

function add_answer(e) {
    e.preventDefault();
    const question = e.target.parentElement.parentElement;
    const id = question.dataset.questionId;
    const input = question.querySelector('#answer');
    fetch(`/answer/${id}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                answer: input.value,
            })
        })
        .then(response => {
            const answer = document.createElement("div");
            answer.classList.add("answer");
            answer.textContent = input.value;
            question.querySelector(".answers").appendChild(answer);
            input.value = "";
        });
}
