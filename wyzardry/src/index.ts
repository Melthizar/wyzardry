// This file is the entry point of the application. It initializes the application and sets up necessary configurations.

import { initializeApp } from './core/constants';
import { AppConfig } from './core/types';

const config: AppConfig = {
    // Add your configuration values here
};

function main() {
    initializeApp(config);
}

main();