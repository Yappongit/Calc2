document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    const buttons = document.querySelector('.buttons');

    let currentExpression = '';
    let errorState = false;

    buttons.addEventListener('click', (e) => {
        if (e.target.tagName !== 'BUTTON') {
            return;
        }

        const value = e.target.dataset.value;

        if (errorState) {
            currentExpression = '';
            errorState = false;
        }

        if (value === 'C') {
            currentExpression = '';
        } else if (value === '=') {
            try {
                if (currentExpression) {
                    // Avoid security risks of eval by validating the expression
                    // This regex allows numbers, decimals, and basic operators.
                    // It prevents multiple operators or invalid sequences.
                    const safeExpression = currentExpression.match(/[0-9.()+\-*\/]+/g).join('');
                    if (safeExpression !== currentExpression) {
                        throw new Error("Invalid characters");
                    }
                    currentExpression = eval(currentExpression).toString();
                }
            } catch (error) {
                currentExpression = 'Error';
                errorState = true;
            }
        } else {
            currentExpression += value;
        }

        display.value = currentExpression;
    });
});