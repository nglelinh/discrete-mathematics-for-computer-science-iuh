/**
 * Interactive Exercise System for Discrete Mathematics
 * Supports multiple choice, true/false, and short answer questions
 */

class ExerciseSystem {
    constructor() {
        this.exercises = new Map();
        this.userProgress = JSON.parse(localStorage.getItem('exerciseProgress') || '{}');
        this.currentScore = 0;
        this.totalQuestions = 0;
        this.init();
    }

    init() {
        this.loadExercises();
        this.bindEvents();
    }

    loadExercises() {
        // Sample exercises for different chapters
        this.exercises.set('logic-basics', {
            title: 'Logic Cơ bản',
            chapter: 'Chương 1',
            questions: [
                {
                    id: 'q1',
                    type: 'multiple-choice',
                    question: 'Mệnh đề nào sau đây là đúng?',
                    options: [
                        '2 + 2 = 5',
                        'Paris là thủ đô của Pháp',
                        'Tất cả số nguyên tố đều là số lẻ',
                        'x + 1 = 5'
                    ],
                    correct: 1,
                    explanation: 'Paris thực sự là thủ đô của Pháp. Các mệnh đề khác đều sai hoặc không phải là mệnh đề.'
                },
                {
                    id: 'q2',
                    type: 'true-false',
                    question: 'Mệnh đề "Nếu trời mưa thì đường ướt" là một mệnh đề kéo theo.',
                    correct: true,
                    explanation: 'Đây là mệnh đề có dạng "Nếu P thì Q", đúng là mệnh đề kéo theo.'
                }
            ]
        });

        this.exercises.set('set-operations', {
            title: 'Phép toán Tập hợp',
            chapter: 'Chương 4',
            questions: [
                {
                    id: 'q3',
                    type: 'multiple-choice',
                    question: 'Cho A = {1, 2, 3} và B = {2, 3, 4}. Tập A ∩ B là:',
                    options: [
                        '{1, 2, 3, 4}',
                        '{2, 3}',
                        '{1, 4}',
                        '∅'
                    ],
                    correct: 1,
                    explanation: 'Giao của A và B là tập hợp các phần tử thuộc cả A và B, tức là {2, 3}.'
                },
                {
                    id: 'q4',
                    type: 'short-answer',
                    question: 'Cho A = {1, 2, 3, 4, 5} và B = {3, 4, 5, 6, 7}. Tính |A ∪ B|.',
                    correct: '7',
                    explanation: 'A ∪ B = {1, 2, 3, 4, 5, 6, 7}, do đó |A ∪ B| = 7.'
                }
            ]
        });
    }

    bindEvents() {
        // Auto-initialize exercises on page load
        document.addEventListener('DOMContentLoaded', () => {
            this.initializePageExercises();
        });
    }

    initializePageExercises() {
        // Look for exercise containers on the page
        const exerciseContainers = document.querySelectorAll('[data-exercise]');
        exerciseContainers.forEach(container => {
            const exerciseId = container.getAttribute('data-exercise');
            if (this.exercises.has(exerciseId)) {
                this.renderExercise(container, exerciseId);
            }
        });
    }

    renderExercise(container, exerciseId) {
        const exercise = this.exercises.get(exerciseId);
        if (!exercise) return;

        const exerciseHTML = `
            <div class="exercise-widget">
                <div class="exercise-header">
                    <h4>${exercise.title}</h4>
                    <span class="exercise-chapter">${exercise.chapter}</span>
                </div>
                <div class="exercise-content">
                    ${exercise.questions.map((q, index) => this.renderQuestion(q, index, exerciseId)).join('')}
                </div>
                <div class="exercise-footer">
                    <button class="btn-submit" onclick="exerciseSystem.submitExercise('${exerciseId}')">
                        Nộp bài
                    </button>
                    <button class="btn-reset" onclick="exerciseSystem.resetExercise('${exerciseId}')">
                        Làm lại
                    </button>
                    <div class="exercise-score" id="score-${exerciseId}"></div>
                </div>
            </div>
        `;

        container.innerHTML = exerciseHTML;
        this.addExerciseStyles();
    }

    renderQuestion(question, index, exerciseId) {
        const questionId = `${exerciseId}-${question.id}`;
        
        switch (question.type) {
            case 'multiple-choice':
                return `
                    <div class="question" data-question-id="${questionId}">
                        <div class="question-text">
                            <strong>Câu ${index + 1}:</strong> ${question.question}
                        </div>
                        <div class="question-options">
                            ${question.options.map((option, i) => `
                                <label class="option">
                                    <input type="radio" name="${questionId}" value="${i}">
                                    <span class="option-text">${option}</span>
                                </label>
                            `).join('')}
                        </div>
                        <div class="question-feedback" id="feedback-${questionId}"></div>
                    </div>
                `;

            case 'true-false':
                return `
                    <div class="question" data-question-id="${questionId}">
                        <div class="question-text">
                            <strong>Câu ${index + 1}:</strong> ${question.question}
                        </div>
                        <div class="question-options">
                            <label class="option">
                                <input type="radio" name="${questionId}" value="true">
                                <span class="option-text">Đúng</span>
                            </label>
                            <label class="option">
                                <input type="radio" name="${questionId}" value="false">
                                <span class="option-text">Sai</span>
                            </label>
                        </div>
                        <div class="question-feedback" id="feedback-${questionId}"></div>
                    </div>
                `;

            case 'short-answer':
                return `
                    <div class="question" data-question-id="${questionId}">
                        <div class="question-text">
                            <strong>Câu ${index + 1}:</strong> ${question.question}
                        </div>
                        <div class="question-input">
                            <input type="text" name="${questionId}" placeholder="Nhập câu trả lời...">
                        </div>
                        <div class="question-feedback" id="feedback-${questionId}"></div>
                    </div>
                `;

            default:
                return '';
        }
    }

    submitExercise(exerciseId) {
        const exercise = this.exercises.get(exerciseId);
        if (!exercise) return;

        let score = 0;
        const totalQuestions = exercise.questions.length;

        exercise.questions.forEach((question, index) => {
            const questionId = `${exerciseId}-${question.id}`;
            const isCorrect = this.checkAnswer(question, questionId);
            
            if (isCorrect) {
                score++;
                this.showFeedback(questionId, true, question.explanation);
            } else {
                this.showFeedback(questionId, false, question.explanation);
            }
        });

        // Update score display
        const scoreElement = document.getElementById(`score-${exerciseId}`);
        const percentage = Math.round((score / totalQuestions) * 100);
        scoreElement.innerHTML = `
            <div class="score-display ${percentage >= 70 ? 'pass' : 'fail'}">
                Điểm: ${score}/${totalQuestions} (${percentage}%)
            </div>
        `;

        // Save progress
        this.userProgress[exerciseId] = {
            score: score,
            total: totalQuestions,
            percentage: percentage,
            timestamp: new Date().toISOString()
        };
        localStorage.setItem('exerciseProgress', JSON.stringify(this.userProgress));

        // Disable form
        this.disableExercise(exerciseId);
    }

    checkAnswer(question, questionId) {
        switch (question.type) {
            case 'multiple-choice':
                const selectedOption = document.querySelector(`input[name="${questionId}"]:checked`);
                return selectedOption && parseInt(selectedOption.value) === question.correct;

            case 'true-false':
                const selectedTF = document.querySelector(`input[name="${questionId}"]:checked`);
                return selectedTF && (selectedTF.value === 'true') === question.correct;

            case 'short-answer':
                const answerInput = document.querySelector(`input[name="${questionId}"]`);
                return answerInput && answerInput.value.trim().toLowerCase() === question.correct.toLowerCase();

            default:
                return false;
        }
    }

    showFeedback(questionId, isCorrect, explanation) {
        const feedbackElement = document.getElementById(`feedback-${questionId}`);
        const icon = isCorrect ? '✅' : '❌';
        const className = isCorrect ? 'correct' : 'incorrect';
        
        feedbackElement.innerHTML = `
            <div class="feedback ${className}">
                ${icon} <strong>${isCorrect ? 'Đúng!' : 'Sai!'}</strong>
                <div class="explanation">${explanation}</div>
            </div>
        `;
    }

    disableExercise(exerciseId) {
        const container = document.querySelector(`[data-exercise="${exerciseId}"]`);
        const inputs = container.querySelectorAll('input');
        inputs.forEach(input => input.disabled = true);
        
        const submitBtn = container.querySelector('.btn-submit');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Đã nộp';
        }
    }

    resetExercise(exerciseId) {
        const container = document.querySelector(`[data-exercise="${exerciseId}"]`);
        
        // Clear all inputs
        const inputs = container.querySelectorAll('input');
        inputs.forEach(input => {
            input.disabled = false;
            if (input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        });

        // Clear feedback
        const feedbacks = container.querySelectorAll('.question-feedback');
        feedbacks.forEach(feedback => feedback.innerHTML = '');

        // Clear score
        const scoreElement = container.querySelector('.exercise-score');
        if (scoreElement) scoreElement.innerHTML = '';

        // Re-enable submit button
        const submitBtn = container.querySelector('.btn-submit');
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Nộp bài';
        }
    }

    addExerciseStyles() {
        if (document.getElementById('exercise-styles')) return;

        const styles = `
            <style id="exercise-styles">
                .exercise-widget {
                    background: white;
                    border: 2px solid #e9ecef;
                    border-radius: 12px;
                    padding: 25px;
                    margin: 25px 0;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                }

                .exercise-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 20px;
                    padding-bottom: 15px;
                    border-bottom: 2px solid #e9ecef;
                }

                .exercise-header h4 {
                    margin: 0;
                    color: #495057;
                    font-size: 1.3em;
                }

                .exercise-chapter {
                    background: #007bff;
                    color: white;
                    padding: 4px 12px;
                    border-radius: 15px;
                    font-size: 0.85em;
                    font-weight: 500;
                }

                .question {
                    margin-bottom: 25px;
                    padding: 20px;
                    background: #f8f9fa;
                    border-radius: 8px;
                    border-left: 4px solid #007bff;
                }

                .question-text {
                    margin-bottom: 15px;
                    font-size: 1.1em;
                    line-height: 1.5;
                }

                .question-options {
                    margin-bottom: 15px;
                }

                .option {
                    display: block;
                    margin-bottom: 10px;
                    padding: 10px 15px;
                    background: white;
                    border: 1px solid #dee2e6;
                    border-radius: 6px;
                    cursor: pointer;
                    transition: all 0.2s ease;
                }

                .option:hover {
                    background: #e3f2fd;
                    border-color: #007bff;
                }

                .option input {
                    margin-right: 10px;
                }

                .question-input input {
                    width: 100%;
                    padding: 12px;
                    border: 1px solid #ced4da;
                    border-radius: 6px;
                    font-size: 16px;
                }

                .question-input input:focus {
                    outline: none;
                    border-color: #007bff;
                    box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
                }

                .feedback {
                    margin-top: 15px;
                    padding: 12px;
                    border-radius: 6px;
                    font-weight: 500;
                }

                .feedback.correct {
                    background: #d4edda;
                    color: #155724;
                    border: 1px solid #c3e6cb;
                }

                .feedback.incorrect {
                    background: #f8d7da;
                    color: #721c24;
                    border: 1px solid #f5c6cb;
                }

                .explanation {
                    margin-top: 8px;
                    font-weight: normal;
                    font-style: italic;
                }

                .exercise-footer {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-top: 25px;
                    padding-top: 20px;
                    border-top: 1px solid #e9ecef;
                }

                .btn-submit, .btn-reset {
                    padding: 12px 24px;
                    border: none;
                    border-radius: 6px;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.2s ease;
                }

                .btn-submit {
                    background: #28a745;
                    color: white;
                }

                .btn-submit:hover:not(:disabled) {
                    background: #218838;
                    transform: translateY(-1px);
                }

                .btn-submit:disabled {
                    background: #6c757d;
                    cursor: not-allowed;
                }

                .btn-reset {
                    background: #6c757d;
                    color: white;
                    margin-left: 10px;
                }

                .btn-reset:hover {
                    background: #5a6268;
                }

                .score-display {
                    font-size: 1.1em;
                    font-weight: bold;
                    padding: 10px 15px;
                    border-radius: 6px;
                }

                .score-display.pass {
                    background: #d4edda;
                    color: #155724;
                }

                .score-display.fail {
                    background: #f8d7da;
                    color: #721c24;
                }

                @media (max-width: 768px) {
                    .exercise-footer {
                        flex-direction: column;
                        gap: 15px;
                    }
                    
                    .exercise-header {
                        flex-direction: column;
                        gap: 10px;
                        text-align: center;
                    }
                }
            </style>
        `;
        document.head.insertAdjacentHTML('beforeend', styles);
    }

    // Helper method to create exercise containers
    static createExerciseContainer(exerciseId) {
        return `<div data-exercise="${exerciseId}"></div>`;
    }
}

// Initialize exercise system
document.addEventListener('DOMContentLoaded', () => {
    window.exerciseSystem = new ExerciseSystem();
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ExerciseSystem;
}
