var participantMonitorResults = [];

Object.entries(localStorage).forEach(([key,val]) => {
    if (key.startsWith("MON-")) {
        participantMonitorResults.push([parseInt(key.slice(4)), parseInt(val)]);
        localStorage.removeItem(key);
    }
});
console.log(participantMonitorResults.toString());
