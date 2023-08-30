const handleKeyPress = async (evt) => {

    const formInputs = {
        'label': 'None',
        'job_id': document.querySelector('#job-id').textContent,
    };

    if (evt.key === 'm') {
        formInputs.label = 1;
    } else if (evt.key === 'z') {
        formInputs.label = 0;
    } else if (evt.key === ' ') {
        // pass
    } else {
        return;
    }
    window.location.href = `/update?label=${formInputs.label}&job_id=${formInputs.job_id}`;
};

document.addEventListener('keyup', handleKeyPress);