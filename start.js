const participantMonitorLabel = document.querySelector('.footer-button__number-counter span');

var participantMonitorTime = Date.now();
console.log(`${participantMonitorLabel.innerHTML} participants at ${participantMonitorTime}`);
localStorage.setItem(`MON-${participantMonitorTime}`, participantMonitorLabel.innerHTML);

participantMonitorLabel.addEventListener('DOMSubtreeModified', () => {
    participantMonitorTime = Date.now();
    console.log(`${participantMonitorLabel.innerHTML} participants at ${participantMonitorTime}`);
    localStorage.setItem(`MON-${participantMonitorTime}`, participantMonitorLabel.innerHTML);
});
