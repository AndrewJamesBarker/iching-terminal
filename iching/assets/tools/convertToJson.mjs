// convertToJson.mjs for use in a node environment, easiest way to make valid JSON from JS object
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Resolve paths
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Import the JS object (must be `export default {...}` in the JS file)
const { default: data } = await import('./assets/iching_wilhelm_translation.js');

// Write to JSON
fs.writeFileSync('/Users/andrewbarker/developer/personal/api-sandbox/client/src/assets/hexagrams_full.json', JSON.stringify(data, null, 2), 'utf-8');
console.log('✅ Converted to src/assets/hexagrams_full.json');
