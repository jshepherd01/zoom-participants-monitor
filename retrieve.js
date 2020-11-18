var participantMonitorResults = [];

Object.entries(localStorage).forEach(([key,val]) => {
    if (key.startsWith("MON-")) {
        participantMonitorResults.push([parseInt(key.slice(4)), parseInt(val)]);
        localStorage.removeItem(key);
    }
});
console.log(participantMonitorResults.toString());

try {
    copy(participantMonitorResults.toString());
    console.log("Copied to clipboard");
} catch(err) {
    console.log("Could not copy to clipboard");
}