export interface Wizard {
    name: string;
    level: number;
    spells: string[];
}

export interface Spell {
    name: string;
    manaCost: number;
    damage: number;
}

export type WizardClass = 'Sorcerer' | 'Necromancer' | 'Elementalist';