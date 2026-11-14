import { promises as fs } from 'fs';
import path from 'path';

export default async function handler(req, res) {
  // Enable CORS so anyone or any app can consume the API
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Cache-Control', 'public, max-age=60, s-maxage=3600, stale-while-revalidate=86400');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    const filePath = path.join(process.cwd(), 'data', 'compact_comics.json');
    const fileContents = await fs.readFile(filePath, 'utf8');
    const data = JSON.parse(fileContents);

    // Return the sorted catalog
    return res.status(200).json({
      success: true,
      lastUpdated: new Date().toISOString(),
      totalTitles: data.length,
      titles: data
    });
  } catch (error) {
    console.error('Error reading comics catalog:', error);
    return res.status(500).json({ success: false, error: 'Failed to read catalog data.' });
  }
}
