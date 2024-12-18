const { exec } = require('child_process');
const fs = require('fs');

// URL to test
const url = 'https://www.nytimes.com/international/section/arts';

// Run Lighthouse
exec(`lighthouse ${url} --output=json --output-path=./lighthouse-report.json`, (err, stdout, stderr) => {
    if (err) {
        console.error(`Error: ${stderr}`);
        return;
    }
    console.log(`Lighthouse report generated: ${stdout}`);
    
    // Read and parse the report
    const report = JSON.parse(fs.readFileSync('./lighthouse-report.json', 'utf8'));
    
    // Extract performance metrics
    const performanceScore = report.categories.performance.score;
    console.log(`Performance Score: ${performanceScore}`);
    
    // Add more metrics as needed
});